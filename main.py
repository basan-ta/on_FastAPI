from typing import Union 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    price : float
    is_offer: Union[bool, None] = None 
    

@app.get("/")
def read_root():
    return {"Hi am learning FastAPi" : "Basan-ta"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    if item_id <0:
        raise HTTPException(status_code=400, detail="Item ID must be a positive integer")
    return {"item_id": item_id, "q": q}

@app.put("/iems/{item_id}:")
def update_item(item_id: int, item: Item):
    return{"item_name" : item.name, "item_id" : item_id}
