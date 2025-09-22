from pydantic import BaseModel, EmailStr, Field

class ClienteCreateInput(BaseModel):
    name: str
    number: str
    email: EmailStr = Field(..., max_length=100)
class ClienteListOutput(ClienteCreateInput):
    id: int

    class Config:
        from_attributes = True  



