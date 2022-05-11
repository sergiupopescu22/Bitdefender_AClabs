from fastapi import FastAPI, File, UploadFile
from typing import Optional
from pydantic import BaseModel
import uvicorn
from enum import Enum

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
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

# @app.post("/upload_files/get_size")
# async def create_file(file: bytes = File(...)):
#     return {"file_size": len(file)}

# @app.post("/upload_file/get_file_name")
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}

@app.post("/upload_files/")
async def create_upload_file(file: Optional[UploadFile] = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}

if __name__ == "__main__":
    uvicorn.run(app)