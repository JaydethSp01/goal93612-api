from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Proveedor(BaseModel):
    id: int
    nombre: str
    contacto: str

# Mock database
proveedores = [
    {"id": 1, "nombre": "Proveedor 1", "contacto": "contacto1@example.com"},
    {"id": 2, "nombre": "Proveedor 2", "contacto": "contacto2@example.com"}
]

@router.get("/proveedor", response_model=List[Proveedor])
async def get_proveedores():
    return proveedores

@router.post("/proveedor", response_model=Proveedor)
async def create_proveedor(proveedor: Proveedor):
    proveedores.append(proveedor.dict())
    return proveedor

@router.put("/proveedor/{proveedor_id}", response_model=Proveedor)
async def update_proveedor(proveedor_id: int, proveedor: Proveedor):
    for p in proveedores:
        if p["id"] == proveedor_id:
            p.update(proveedor.dict())
            return proveedor
    raise HTTPException(status_code=404, detail="Proveedor not found")

@router.delete("/proveedor/{proveedor_id}")
async def delete_proveedor(proveedor_id: int):
    for p in proveedores:
        if p["id"] == proveedor_id:
            proveedores.remove(p)
            return {"message": "Proveedor deleted"}
    raise HTTPException(status_code=404, detail="Proveedor not found")