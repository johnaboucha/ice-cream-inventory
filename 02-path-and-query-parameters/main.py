from fastapi import FastAPI, Path, Query
from inventory import inventory

app = FastAPI()

@app.get("/")
def root():
	return inventory

@app.get("/items/")
def get_items(vegan: bool = False, max_price: float = Query(default=20, ge=1)):
	results = {}
	counter = 1
	for item in inventory.values():
		if item["vegan"] == vegan and item["price"] <= max_price:
			results[counter] = item
			counter += 1
	return results

@app.get("/items/{id}")
def get_item(id: int):
    return inventory[id]

