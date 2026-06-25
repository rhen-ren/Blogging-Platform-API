from fastapi import FastAPI, APIRouter
from router import blogpost
from db import Base, engine
from model import post, category, tag, posttags
import uvicorn

app = FastAPI()
app.include_router(blogpost.router)

Base.metadata.create_all(bind=engine)




if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
