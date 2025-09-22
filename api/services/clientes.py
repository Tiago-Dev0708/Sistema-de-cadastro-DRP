from sqlalchemy.future import select
from sqlalchemy import delete
from api.database.models.clientes import Cliente
from api.database.connection.connection import async_session

class ClienteService:
    @staticmethod
    async def create_client(cliente: Cliente):
        async with async_session() as session:
            async with session.begin():
                session.add(cliente)
                await session.commit()

    @staticmethod
    async def list_client_by_id(cliente_id: int):
        async with async_session() as session:
            result = await session.execute(select(Cliente).where(Cliente.id == cliente_id))
            return result.scalars().first()

    @staticmethod
    async def list_clients():
        async with async_session() as session:
            result = await session.execute(select(Cliente))
            return result.scalars().all()
        
    @staticmethod
    async def delete_client(cliente_id: int):
        async with async_session() as session:
            async with session.begin():
                await session.execute(delete(Cliente).where(Cliente.id == cliente_id))
                await session.commit()
