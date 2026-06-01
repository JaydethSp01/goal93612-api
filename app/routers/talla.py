from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Talla(BaseModel):
    id: int
    nombre: str

# Mock database

@router.get("/talla", response_model=List[Talla])
async def get_tallas():
    return tallas

@router.post("/talla", response_model=Talla)
async def create_talla(talla: Talla):
    tallas.append(talla.dict())
    return talla

@router.put("/talla/{talla_id}", response_model=Talla)
async def update_talla(talla_id: int, talla: Talla):
    for t in tallas:
        if t["id"] == talla_id:
            t.update(talla.dict())
            return talla
    raise HTTPException(status_code=404, detail="Talla not found")

@router.delete("/talla/{talla_id}")
async def delete_talla(talla_id: int):
    for t in tallas:
        if t["id"] == talla_id:
            tallas.remove(t)
            return {"message": "Talla deleted"}
    raise HTTPException(status_code=404, detail="Talla not found")