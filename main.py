from fastapi import FastAPI, APIRouter
from router import blogpost
import uvicorn

app = FastAPI()

app.include_router(blogpost.router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)