from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    categoria_id: int

# Mock database
productos = [
    {"id": 1, "nombre": "Camiseta", "precio": 19.99, "categoria_id": 1},
    {"id": 2, "nombre": "Jeans", "precio": 49.99, "categoria_id": 2}
]

@router.get("/producto", response_model=List[Producto])
async def get_productos():
    return productos

@router.post("/producto", response_model=Producto)
async def create_producto(producto: Producto):
    productos.append(producto.dict())
    return producto

@router.put("/producto/{producto_id}", response_model=Producto)
async def update_producto(producto_id: int, producto: Producto):
    for p in productos:
        if p["id"] == producto_id:
            p.update(producto.dict())
            return producto
    raise HTTPException(status_code=404, detail="Producto not found")

@router.delete("/producto/{producto_id}")
async def delete_producto(producto_id: int):
    for p in productos:
        if p["id"] == producto_id:
            productos.remove(p)
            return {"message": "Producto deleted"}
    raise HTTPException(status_code=404, detail="Producto not found")