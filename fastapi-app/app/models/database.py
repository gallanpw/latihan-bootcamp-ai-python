import uuid
from sqlmodel import SQLModel, Field

class Product(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    name: str = Field(default="Product...")
    description: str = Field(default="Description...")