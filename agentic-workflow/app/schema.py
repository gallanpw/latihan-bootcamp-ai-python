from pydantic import BaseModel, Field


class QueriesSchema(BaseModel):
    queries: list[str] = Field(
        description="List of queries generated for the given topic"
    )
