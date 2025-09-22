from fastapi import APIRouter, HTTPException
from typing import List

from api.schemas.clientes import ClienteCreateInput, ClienteListOutput
from api.schemas.StandardOutputs_Errors import StandardOutput, ErrorOutput
from api.services.clientes import ClienteService
from api.database.models.clientes import Cliente

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/adicionar", response_model=StandardOutput, responses={400: {"model": ErrorOutput}})
async def create_client(cliente: ClienteCreateInput):
    try:
        cliente_model = Cliente(name=cliente.name,
                                number=cliente.number,
                                email=cliente.email,
                               )
        await ClienteService.create_client(cliente_model)
        return StandardOutput(message="Cliente criado com sucesso")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/deletar/{cliente_id}", response_model=StandardOutput, responses={400: {"model": ErrorOutput}})
async def delete_client(cliente_id: int):
    try:
        await ClienteService.delete_client(cliente_id)
        return StandardOutput(message="Cliente deletado com sucesso")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/listar", response_model=List[ClienteListOutput], responses={400: {"model": ErrorOutput}})
async def list_clients():
    try:
        clients = await ClienteService.list_clients()
        return clients
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
