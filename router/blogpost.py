from fastapi import FastAPI, APIRouter, Body, Depends
from fastapi.responses import JSONResponse
from schema.post import CreatePost, GetPost
from dependency import run_db
from service import blogpostservices
from testData import testData
from sqlalchemy.orm import Session


router = APIRouter(prefix="/blogpost")


@router.get("/posts")
def get_posts() -> CreatePost:
    return testData

@router.post("/posts")
def create_post(post: CreatePost, db: Session = Depends(run_db)):
    return blogpostservices.create_post(post, db)

@router.put("/posts/{post_id}")
def create_post(post: CreatePost, post_id: int, db:Session = Depends(run_db)):
    return blogpostservices.update_post(post, post_id, db)