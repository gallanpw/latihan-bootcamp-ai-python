from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from fastapi.openapi.utils import status_code_ranges
from app.utils.query_params import standard_params
from app.schema.product import ProductResponse, ProductRequest
from app.schema.auth import LoginRequest
from fastapi import APIRouter, Query, Header, Depends, HTTPException, status

auth_router = APIRouter(tags=["Auth"])

@auth_router.post(path="/login")
def login(body: LoginRequest):

    email: str = body.email
    password: str = body.password
    
    if email != "gallan@email.com":
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Email Not Found")

    if password != "admin123":
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Invalid Password")

    return {"message": "Good!"}