from fastapi import FastAPI, APIRouter
from router import blogpost
from db import Base, engine
import uvicorn

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(blogpost.router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
