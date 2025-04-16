from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Модель товара
class Product(BaseModel):
    id: int
    name: str
    description: str

# Временное хранилище для товаров (вместо базы данных)
products_db = []

@router.get("/products/", response_model=List[Product])
async def read_products():
    return products_db

@router.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int):
    for product in products_db:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@router.post("/products/", response_model=Product)
async def create_product(product: Product):
    products_db.append(product)
    return product