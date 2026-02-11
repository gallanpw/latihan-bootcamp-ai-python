from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    password: str

# class ProductResponse(BaseModel):
#     id: str
#     name: str
#     description: str | None = None
#     price: float | None = None