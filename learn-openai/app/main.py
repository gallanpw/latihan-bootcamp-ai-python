from fastapi import FastAPI
from app.modules.stories.router import stories_router

app = FastAPI()

app.include_router(router=stories_router)