import sys, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from fastapi import FastAPI, File, UploadFile
from typing import Optional
from pydantic import BaseModel
import aiohttp
import uvicorn
from Scan_files.test_mongo_db import TestDatabase

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    ID: int

ItemList = []

app = FastAPI()

@app.get("/")
def get_basic_info():
    return {"message":"Welcome to our server!"}

@app.post("/adaugare_items/")
async def create_item(item: Item):
    ItemList.append(item)
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int):
    for i in ItemList:
        if i.ID == item_id:
            return {"message": "Item found", "item":i}
    return {"Message": "Could not fing an item with this ID"}

@app.post("/upload_files/")
async def create_upload_file(file: Optional[UploadFile] = None):
    if not file:
        return "No file detected"#{"filename": file.filename}
    else:
        async with aiohttp.ClientSession() as session:
            async with session.post('https://beta.nimbus.bitdefender.net:443/liga-ac-labs-cloud/blackbox-scanner/',
                                    data={'file': await file.read()}) as response:
                res = await response.json()
                db = TestDatabase()
                await db.insert_data(res)
                return res


if __name__ == "__main__":
    #uvicorn.run(app, host='0.0.0.0', port=8001)
    uvicorn.run(app, port=8001)

