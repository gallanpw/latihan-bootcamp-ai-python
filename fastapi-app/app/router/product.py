from app.models.database import Product
from sqlmodel import select
from app.models.engine import get_db
from app.utils.query_params import standard_params
from app.schema.product import ProductResponse, ProductRequest
from fastapi import APIRouter, Query, Header, Depends, status

product_router = APIRouter(tags=["Products"])

@product_router.get(path="/products", status_code=status.HTTP_200_OK)
# def get_products(limit: int = Query(default=10, gt=5), offset: int | None = None):
def get_products(params = Depends(standard_params), db = Depends(get_db)):
    # cocok ketika butuh plain data
    
    stmt = select(Product)
    result = db.exec(stmt)
    products = result.all()
    
    # return ProductResponse(
    #     id="1",
    #     name="Product name",
    #     description="Product Description",
    #     price=10.0
    # )
    # return {"params": params}
    return products

@product_router.post(path="/products", status_code=status.HTTP_201_CREATED)
def create_products(body: ProductRequest, db = Depends(get_db)):
    # return ProductResponse(
    #     id="1",
    #     name="Product name",
    #     description="Product Description",
    #     price=10.0
    # )

    try:
        new_product = Product(name=body.name, description=body.description)
        db.add(new_product)
        db.commit()
        db.refresh(new_product)

        return { "message": "Product created Successfully!", "product": new_product }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
