from pydantic import BaseModel

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    categoria_id: int
    proveedor_id: int

class Categoria(BaseModel):
    id: int
    nombre: str

class Proveedor(BaseModel):
    id: int
    nombre: str
    contacto: str

class Stock(BaseModel):
    id: int
    producto_id: int
    talla_id: int
    cantidad: int

class Talla(BaseModel):
    id: int
    nombre: str

class Alerta(BaseModel):
    id: int
    producto_id: int
    mensaje: str