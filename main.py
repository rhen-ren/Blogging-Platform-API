from fastapi import FastApi, APIRouter
from router import blogpost

app = FastApi()

app.include_router(blogpost.router)


