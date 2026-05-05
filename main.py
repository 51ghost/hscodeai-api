"""HSCodeAI API — Harmonized System Tariff Classification"""
import os, logging
from typing import Optional
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from data_pipeline import HS_CODES, search_hscodes, get_hscode_detail, get_duty_rate, SECTIONS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("hscodeai")

app = FastAPI(title="HSCodeAI API", version="1.0.0", description="Real USITC Harmonized Tariff Schedule — 500+ HS codes with duty rates, sections, and country-specific rules")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

API_KEYS = {os.environ.get("INTERNAL_API_KEY", "demo-key")}

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    if request.url.path in ["/health", "/docs", "/openapi.json"]:
        return await call_next(request)
    key = request.headers.get("x-api-key", "")
    if key not in API_KEYS:
        from fastapi.responses import JSONResponse
        return JSONResponse({"detail": "Invalid or missing API key"}, status_code=401)
    return await call_next(request)

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "HSCodeAI", "codes": len(HS_CODES)}

@app.get("/v1/hscodes/search")
async def search(q: str = Query(""), section: Optional[str] = Query(None), limit: int = Query(20, le=100)):
    results = search_hscodes(q, section, limit)
    return {"total": len(results), "results": results}

@app.get("/v1/hscodes/{code}")
async def detail(code: str):
    result = get_hscode_detail(code)
    if not result: raise HTTPException(404, f"HS code {code} not found")
    return result

@app.get("/v1/duty/{code}")
async def duty(code: str, origin: str = Query("CN"), destination: str = Query("US")):
    result = get_duty_rate(code, origin, destination)
    if "error" in result: raise HTTPException(404, result["error"])
    return result

@app.get("/v1/sections")
async def sections():
    return {"sections": [{"id": s["id"], "title": s["title"]} for s in SECTIONS]}

@app.get("/v1/sections/{section_id}")
async def section_detail(section_id: str):
    from data_pipeline import SECTIONS
    for s in SECTIONS:
        if s["id"] == section_id: return s
    raise HTTPException(404, f"Section {section_id} not found")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
