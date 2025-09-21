from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api.database.models import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(String(11))
    name = Column(String(100))
    email = Column(String(100))

    pedidos = relationship("Pedido", back_populates="clientes")
