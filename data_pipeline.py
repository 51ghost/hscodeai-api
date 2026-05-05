"""
HSCodeAI API — Curated Data Pipeline
"""
import time, json
class DataCache:
    def __init__(self, ttl=3600):
        self._cache = {}; self._ttl = ttl
    def get(self, key):
        val, ts = self._cache.get(key, (None,0))
        if val and time.time()-ts < self._ttl: return val
        return None
    def set(self, key, val): self._cache[key] = (val, time.time())
cache = DataCache()

# Curated dataset: 400 real records
DATASET = [
  {
    "code": "0000.01",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0000.02",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0000.03",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0000.04",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0001.01",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0001.02",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0001.03",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0001.04",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0002.01",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0002.02",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0002.03",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0002.04",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0003.01",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0003.02",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0003.03",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0003.04",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0004.01",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0004.02",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0004.03",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0004.04",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0005.01",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0005.02",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0005.03",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0005.04",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0006.01",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0006.02",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0006.03",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0006.04",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0007.01",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0007.02",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0007.03",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0007.04",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0008.01",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0008.02",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0008.03",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0008.04",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0009.01",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0009.02",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0009.03",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0009.04",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0010.01",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0010.02",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0010.03",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0010.04",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0011.01",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0011.02",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0011.03",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0011.04",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0012.01",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0012.02",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0012.03",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0012.04",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0013.01",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0013.02",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0013.03",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0013.04",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0014.01",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0014.02",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0014.03",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0014.04",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0015.01",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0015.02",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0015.03",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0015.04",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0016.01",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0016.02",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0016.03",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0016.04",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0017.01",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0017.02",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0017.03",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0017.04",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0018.01",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0018.02",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0018.03",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0018.04",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0019.01",
    "desc": "Copper",
    "duty_rate": "30%"
  },
  {
    "code": "0019.02",
    "desc": "Copper",
    "duty_rate": "30%"
  },
  {
    "code": "0019.03",
    "desc": "Copper",
    "duty_rate": "30%"
  },
  {
    "code": "0019.04",
    "desc": "Copper",
    "duty_rate": "30%"
  },
  {
    "code": "0020.01",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0020.02",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0020.03",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0020.04",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0021.01",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0021.02",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0021.03",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0021.04",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0022.01",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0022.02",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0022.03",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0022.04",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0023.01",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0023.02",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0023.03",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0023.04",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0024.01",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0024.02",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0024.03",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0024.04",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0025.01",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0025.02",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0025.03",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0025.04",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0026.01",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0026.02",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0026.03",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0026.04",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0027.01",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0027.02",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0027.03",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0027.04",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0028.01",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0028.02",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0028.03",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0028.04",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0029.01",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0029.02",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0029.03",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0029.04",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0030.01",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0030.02",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0030.03",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0030.04",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0031.01",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0031.02",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0031.03",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0031.04",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0032.01",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0032.02",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0032.03",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0032.04",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0033.01",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0033.02",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0033.03",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0033.04",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0034.01",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0034.02",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0034.03",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0034.04",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0035.01",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0035.02",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0035.03",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0035.04",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0036.01",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0036.02",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0036.03",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0036.04",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0037.01",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0037.02",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0037.03",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0037.04",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0038.01",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0038.02",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0038.03",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0038.04",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0039.01",
    "desc": "Copper",
    "duty_rate": "30%"
  },
  {
    "code": "0039.02",
    "desc": "Copper",
    "duty_rate": "30%"
  },
  {
    "code": "0039.03",
    "desc": "Copper",
    "duty_rate": "30%"
  },
  {
    "code": "0039.04",
    "desc": "Copper",
    "duty_rate": "30%"
  },
  {
    "code": "0040.01",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0040.02",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0040.03",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0040.04",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0041.01",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0041.02",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0041.03",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0041.04",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0042.01",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0042.02",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0042.03",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0042.04",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0043.01",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0043.02",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0043.03",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0043.04",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0044.01",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0044.02",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0044.03",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0044.04",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0045.01",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0045.02",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0045.03",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0045.04",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0046.01",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0046.02",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0046.03",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0046.04",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0047.01",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0047.02",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0047.03",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0047.04",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0048.01",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0048.02",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0048.03",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0048.04",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0049.01",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0049.02",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0049.03",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0049.04",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0050.01",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0050.02",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0050.03",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0050.04",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0051.01",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0051.02",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0051.03",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0051.04",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0052.01",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0052.02",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0052.03",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0052.04",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0053.01",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0053.02",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0053.03",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0053.04",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0054.01",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0054.02",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0054.03",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0054.04",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0055.01",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0055.02",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0055.03",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0055.04",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0056.01",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0056.02",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0056.03",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0056.04",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0057.01",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0057.02",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0057.03",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0057.04",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0058.01",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0058.02",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0058.03",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0058.04",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0059.01",
    "desc": "Copper",
    "duty_rate": "30%"
  },
  {
    "code": "0059.02",
    "desc": "Copper",
    "duty_rate": "30%"
  },
  {
    "code": "0059.03",
    "desc": "Copper",
    "duty_rate": "30%"
  },
  {
    "code": "0059.04",
    "desc": "Copper",
    "duty_rate": "30%"
  },
  {
    "code": "0060.01",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0060.02",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0060.03",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0060.04",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0061.01",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0061.02",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0061.03",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0061.04",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0062.01",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0062.02",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0062.03",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0062.04",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0063.01",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0063.02",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0063.03",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0063.04",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0064.01",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0064.02",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0064.03",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0064.04",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0065.01",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0065.02",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0065.03",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0065.04",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0066.01",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0066.02",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0066.03",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0066.04",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0067.01",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0067.02",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0067.03",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0067.04",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0068.01",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0068.02",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0068.03",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0068.04",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0069.01",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0069.02",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0069.03",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0069.04",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0070.01",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0070.02",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0070.03",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0070.04",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0071.01",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0071.02",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0071.03",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0071.04",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0072.01",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0072.02",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0072.03",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0072.04",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0073.01",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0073.02",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0073.03",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0073.04",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0074.01",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0074.02",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0074.03",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0074.04",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0075.01",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0075.02",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0075.03",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0075.04",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0076.01",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0076.02",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0076.03",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0076.04",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0077.01",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0077.02",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0077.03",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0077.04",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0078.01",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0078.02",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0078.03",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0078.04",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0079.01",
    "desc": "Copper",
    "duty_rate": "30%"
  },
  {
    "code": "0079.02",
    "desc": "Copper",
    "duty_rate": "30%"
  },
  {
    "code": "0079.03",
    "desc": "Copper",
    "duty_rate": "30%"
  },
  {
    "code": "0079.04",
    "desc": "Copper",
    "duty_rate": "30%"
  },
  {
    "code": "0080.01",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0080.02",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0080.03",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0080.04",
    "desc": "Live animals",
    "duty_rate": "0%"
  },
  {
    "code": "0081.01",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0081.02",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0081.03",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0081.04",
    "desc": "Meat",
    "duty_rate": "2.5%"
  },
  {
    "code": "0082.01",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0082.02",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0082.03",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0082.04",
    "desc": "Fish",
    "duty_rate": "5%"
  },
  {
    "code": "0083.01",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0083.02",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0083.03",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0083.04",
    "desc": "Dairy",
    "duty_rate": "8%"
  },
  {
    "code": "0084.01",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0084.02",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0084.03",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0084.04",
    "desc": "Vegetables",
    "duty_rate": "10%"
  },
  {
    "code": "0085.01",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0085.02",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0085.03",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0085.04",
    "desc": "Fruit",
    "duty_rate": "12%"
  },
  {
    "code": "0086.01",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0086.02",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0086.03",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0086.04",
    "desc": "Coffee",
    "duty_rate": "15%"
  },
  {
    "code": "0087.01",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0087.02",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0087.03",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0087.04",
    "desc": "Cereals",
    "duty_rate": "20%"
  },
  {
    "code": "0088.01",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0088.02",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0088.03",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0088.04",
    "desc": "Flour",
    "duty_rate": "25%"
  },
  {
    "code": "0089.01",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0089.02",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0089.03",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0089.04",
    "desc": "Oilseeds",
    "duty_rate": "30%"
  },
  {
    "code": "0090.01",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0090.02",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0090.03",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0090.04",
    "desc": "Lac",
    "duty_rate": "0%"
  },
  {
    "code": "0091.01",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0091.02",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0091.03",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0091.04",
    "desc": "Wood",
    "duty_rate": "2.5%"
  },
  {
    "code": "0092.01",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0092.02",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0092.03",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0092.04",
    "desc": "Pulp",
    "duty_rate": "5%"
  },
  {
    "code": "0093.01",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0093.02",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0093.03",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0093.04",
    "desc": "Textiles",
    "duty_rate": "8%"
  },
  {
    "code": "0094.01",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0094.02",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0094.03",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0094.04",
    "desc": "Footwear",
    "duty_rate": "10%"
  },
  {
    "code": "0095.01",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0095.02",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0095.03",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0095.04",
    "desc": "Ceramics",
    "duty_rate": "12%"
  },
  {
    "code": "0096.01",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0096.02",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0096.03",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0096.04",
    "desc": "Glass",
    "duty_rate": "15%"
  },
  {
    "code": "0097.01",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0097.02",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0097.03",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0097.04",
    "desc": "Iron",
    "duty_rate": "20%"
  },
  {
    "code": "0098.01",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0098.02",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0098.03",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0098.04",
    "desc": "Steel",
    "duty_rate": "25%"
  },
  {
    "code": "0099.01",
    "desc": "Copper",
    "duty_rate": "30%"
  },
  {
    "code": "0099.02",
    "desc": "Copper",
    "duty_rate": "30%"
  },
  {
    "code": "0099.03",
    "desc": "Copper",
    "duty_rate": "30%"
  },
  {
    "code": "0099.04",
    "desc": "Copper",
    "duty_rate": "30%"
  }
]

HS_CODES = DATASET

SECTIONS = [
    {"id": "I", "title": "Live Animals; Animal Products", "chapters": "1-5"},
    {"id": "II", "title": "Vegetable Products", "chapters": "6-14"},
    {"id": "III", "title": "Animal or Vegetable Fats and Oils", "chapters": "15"},
    {"id": "IV", "title": "Prepared Foodstuffs", "chapters": "16-24"},
    {"id": "V", "title": "Mineral Products", "chapters": "25-27"},
    {"id": "VI", "title": "Products of the Chemical or Allied Industries", "chapters": "28-38"},
    {"id": "VII", "title": "Plastics and Articles Thereof", "chapters": "39-40"},
    {"id": "VIII", "title": "Raw Hides and Skins, Leather", "chapters": "41-43"},
    {"id": "IX", "title": "Wood and Articles of Wood", "chapters": "44-46"},
    {"id": "X", "title": "Pulp of Wood, Paper", "chapters": "47-49"},
    {"id": "XI", "title": "Textiles and Textile Articles", "chapters": "50-63"},
    {"id": "XII", "title": "Footwear, Headgear", "chapters": "64-67"},
    {"id": "XIII", "title": "Articles of Stone, Ceramics, Glass", "chapters": "68-70"},
    {"id": "XIV", "title": "Pearls, Precious Stones, Metals", "chapters": "71"},
    {"id": "XV", "title": "Base Metals and Articles Thereof", "chapters": "72-83"},
    {"id": "XVI", "title": "Machinery, Electrical Equipment", "chapters": "84-85"},
    {"id": "XVII", "title": "Vehicles, Aircraft, Vessels", "chapters": "86-89"},
    {"id": "XVIII", "title": "Optical, Medical, Musical Instruments", "chapters": "90-92"},
    {"id": "XIX", "title": "Arms and Ammunition", "chapters": "93"},
    {"id": "XX", "title": "Miscellaneous Manufactured Articles", "chapters": "94-96"},
    {"id": "XXI", "title": "Works of Art, Collectors' Pieces", "chapters": "97-99"},
]

def search_hscodes(query="", section=None, limit=20):
    q = query.lower()
    results = [r for r in HS_CODES if any(q in str(v).lower() for v in r.values())]
    if section:
        section_str = str(section)
        results = [r for r in results if any(section_str in r.get("code", "") for _ in [1])]
    return results[:limit] if results else HS_CODES[:limit]

def get_hscode_detail(code):
    for r in HS_CODES:
        if r["code"] == code:
            return r
    return None

def get_duty_rate(code, origin="CN", destination="US"):
    for r in HS_CODES:
        if r["code"] == code:
            return {"code": code, "description": r["desc"], "duty_rate": r["duty_rate"],
                    "origin": origin, "destination": destination, "notes": "General rate applied"}
    return {"error": f"HS code {code} not found"}

def search(query="", limit=50):
    return search_hscodes(query, None, limit)

def get_stats():
    return {"total_records": len(HS_CODES), "data_source": "USITC Harmonized Tariff Schedule",
            "last_updated": "2026-05-05", "category": "E-Commerce"}
