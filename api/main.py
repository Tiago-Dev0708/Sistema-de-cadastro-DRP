from fastapi import FastAPI
from api.database.connection.connection import engine
from contextlib import asynccontextmanager
from api.database.models import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)  
