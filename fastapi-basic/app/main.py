from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from app.modules.products.serializer import ProductResponse, CreateProductResponse

app = FastAPI(
    docs_url=None,
    redoc_url=None
)

@app.get(path="/hello")
def say_hello():
    return {"message": "hello!"}

@app.get(path="/products", tags=["products"])
def get_products():
    return { "product": {} }

@app.get(path="/products/{id}", tags=["products"], response_model=ProductResponse)
def get_product_by_id(id: int):
    return ProductResponse(id=id, name=f"product-{id}", price=100.0 * id, description= f"description {id}")

@app.post(path="/products", tags=["products"], response_model=ProductResponse)
def create_product(body: CreateProductResponse):
    new_id = 1
    return {"id":new_id, "name":body.name, "price":body.price, "description":body.description}
    # return {"product": {"id": new_id, "name": body.name, "price": body.price , "description": body.description}}


@app.patch(path="/products/{id}", tags=["products"])
def update_product():
    return { "product": {} }

@app.delete(path="/products/{id}", tags=["products"])
def delete_product():
    return { "product": {} }

@app.get(path="/scalar")
def scalar_doc():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url
    )