from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class PedidoCreateInput(BaseModel):
    produto: str
    valor: int
    data_compra: date

class PedidoListOutput(PedidoCreateInput):
    id: int

    class Config:
        from_attributes = True  



