from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Stock(BaseModel):
    id: int
    producto_id: int
    talla_id: int
    cantidad: int

# Mock database
stocks = [
    {"id": 1, "producto_id": 1, "talla_id": 1, "cantidad": 50},
    {"id": 2, "producto_id": 2, "talla_id": 2, "cantidad": 30}
]

@router.get("/stock", response_model=List[Stock])
async def get_stocks():
    return stocks

@router.post("/stock", response_model=Stock)
async def create_stock(stock: Stock):
    stocks.append(stock.dict())
    return stock

@router.put("/stock/{stock_id}", response_model=Stock)
async def update_stock(stock_id: int, stock: Stock):
    for s in stocks:
        if s["id"] == stock_id:
            s.update(stock.dict())
            return stock
    raise HTTPException(status_code=404, detail="Stock not found")

@router.delete("/stock/{stock_id}")
async def delete_stock(stock_id: int):
    for s in stocks:
        if s["id"] == stock_id:
            stocks.remove(s)
            return {"message": "Stock deleted"}
    raise HTTPException(status_code=404, detail="Stock not found")