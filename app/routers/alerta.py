from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Alerta(BaseModel):
    id: int
    producto_id: int
    talla_id: int
    mensaje: str

# Mock database
alertas = [
    {"id": 1, "producto_id": 1, "talla_id": 1, "mensaje": "Stock bajo"},
    {"id": 2, "producto_id": 2, "talla_id": 2, "mensaje": "Sin stock"}
]

@router.get("/alerta", response_model=List[Alerta])
async def get_alertas():
    return alertas

@router.post("/alerta", response_model=Alerta)
async def create_alerta(alerta: Alerta):
    alertas.append(alerta.dict())
    return alerta

@router.put("/alerta/{alerta_id}", response_model=Alerta)
async def update_alerta(alerta_id: int, alerta: Alerta):
    for a in alertas:
        if a["id"] == alerta_id:
            a.update(alerta.dict())
            return alerta
    raise HTTPException(status_code=404, detail="Alerta not found")

@router.delete("/alerta/{alerta_id}")
async def delete_alerta(alerta_id: int):
    for a in alertas:
        if a["id"] == alerta_id:
            alertas.remove(a)
            return {"message": "Alerta deleted"}
    raise HTTPException(status_code=404, detail="Alerta not found")