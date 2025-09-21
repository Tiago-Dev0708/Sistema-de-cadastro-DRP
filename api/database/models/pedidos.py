from sqlalchemy import Column, Integer, ForeignKey, Date, String
from sqlalchemy.orm import relationship
from datetime import date
from api.database.models import Base

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    produto = Column(String(100))
    valor = Column(Integer)
    data_compra = Column(Date, default=date.today())  

    clientes = relationship("Cliente", back_populates="pedidos")
