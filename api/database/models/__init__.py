from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


from .clientes import Cliente
from .pedidos import Pedido

