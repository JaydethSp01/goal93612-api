from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Categoria(BaseModel):
    id: int
    nombre: str

# Mock database
categorias = [
    {"id": 1, "nombre": "Ropa Casual"},
    {"id": 2, "nombre": "Ropa Formal"}
]

@router.get("/categoria", response_model=List[Categoria])
async def get_categorias():
    return categorias

@router.post("/categoria", response_model=Categoria)
async def create_categoria(categoria: Categoria):
    categorias.append(categoria.dict())
    return categoria

@router.put("/categoria/{categoria_id}", response_model=Categoria)
async def update_categoria(categoria_id: int, categoria: Categoria):
    for c in categorias:
        if c["id"] == categoria_id:
            c.update(categoria.dict())
            return categoria
    raise HTTPException(status_code=404, detail="Categoria not found")

@router.delete("/categoria/{categoria_id}")
async def delete_categoria(categoria_id: int):
    for c in categorias:
        if c["id"] == categoria_id:
            categorias.remove(c)
            return {"message": "Categoria deleted"}
    raise HTTPException(status_code=404, detail="Categoria not found")