from pydantic import BaseModel

class ProductRequest(BaseModel):
    name: str
    description: str | None = None
    # price: float | None = None

class ProductResponse(BaseModel):
    id: str
    name: str
    description: str | None = None
    # price: float | None = None