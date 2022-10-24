from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from inventory import inventory

class Item(BaseModel):
	flavor: str
	description: str
	price: float
	vegan: bool
	quantity: int

app = FastAPI()

@app.get("/items/")
def root():
	return inventory

@app.get("/items/{id}/")
def get_item(id: int):
	if id not in inventory:
		raise HTTPException(status_code=404, detail="Ice cream ID not found")
	return inventory[id]

@app.post("/items/")
def create_item(item: Item):
	inventory[len(inventory)+1] = item.dict()
	return inventory

@app.put("/items/{id}/")
def update_item(id: int, item: Item):
	if id not in inventory:
		raise HTTPException(status_code=404, detail="Ice cream ID not found")
	inventory[id] = item.dict()
	return inventory

@app.delete("/items/{id}/")
def delete_item(id: int):
	if id not in inventory:
		raise HTTPException(status_code=404, detail="Ice cream ID not found")
	del inventory[id]
	return inventory