from app.utils.query_params import standard_params
from app.schema.product import ProductResponse, ProductRequest
from fastapi import APIRouter, Query, Header, Depends

stores_router = APIRouter(tags=["Stores"])

@stores_router.get(path="/stores")
# def get_products(limit: int = Query(default=10, gt=5), offset: int | None = None):
def get_stores(params = Depends(dependency=standard_params)):
    # cocok ketika butuh plain data
    # return ProductResponse(
    #     id="1",
    #     name="Product name",
    #     description="Product Description",
    #     price=10.0
    # )
    return {"params": params}

@stores_router.post(path="/stores")
def create_stores(body: ProductRequest):
    return ProductResponse(
        id="1",
        name="Product name",
        description="Product Description",
        price=10.0
    )