from fastapi import FastAPI, HTTPException

from pydantic import BaseModel


# uvicorn main:app --reload

app = FastAPI()

class Product(BaseModel):
    id: int
    item: str
    description: str | None = None
    price: float

# fake data base
fake_db = [Product(id=1, item="Phone", description="", price=699.99),
           Product(id=2, item="TV", description="This is a good TV", price=279.99),
           Product(id=3, item="Smart Watch", description="Ultimate gen of tech", price=359.99),]

# Get all products
@app.get("/products/")
async def products():
    return fake_db

# Path id
@app.get("/item/{id}")
async def item(id: int):
    return search_id(id)

# name item query
@app.get("/item/")
async def item(item: str):
    return search_item(item)

# Create new product
@app.post("/item/")
async def create_item(item: Product):
    if type(search_id(item.id)) == Product:
        return {"error": "El producto ya existe"}
    fake_db.append(item)
    return item

# Update product
@app.put("/item/")
async def update_item(item: Product):

    for index, product in enumerate(fake_db):
        if product.id == item.id:
            fake_db[index] = item

    return item

# Delete product
@app.delete("/item/")
async def delete_item(id: int):
    
    for index, product in enumerate(fake_db):
        if product.id == id:
            del fake_db[index]

    return {"200": "Se ha eliminado el producto"}

# Search id
def search_id(id: int):
    products = filter(lambda product: product.id == id, fake_db)
    try:
        return list(products)[0]
    except:
        return {"error":"No se ha encontrado el id"}

# Search item
def search_item(item: str):
    products = filter(lambda product: product.item == item, fake_db)
    try:
        return list(products)[0]
    except:
        return {"error":"No se han encontrado el producto"}
