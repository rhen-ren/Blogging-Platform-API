from fastapi import FastAPI, APIRouter, Body, Depends
from fastapi.responses import JSONResponse
from schema.post import CreatePost, GetPost
from dependency import run_db
from service import blogpostservices
from testData import testData
from sqlalchemy.orm import Session


router = APIRouter(prefix="/blogpost")


@router.get("/posts")
def get_posts(db: Session = Depends(run_db)) -> list[GetPost]:
    return blogpostservices.get_all_posts(db)

@router.get("/posts/{post_id}")
def create_post(post_id: int, db:Session = Depends(run_db)):
    return blogpostservices.get_post(post_id, db)

@router.delete("/posts/{post_id}")
def create_post(post_id: int, db:Session = Depends(run_db)):
    return blogpostservices.delete_post(post_id, db)

@router.post("/posts")
def create_post(post: CreatePost, db: Session = Depends(run_db)):
    return blogpostservices.create_post(post, db)

@router.put("/posts/{post_id}")
def create_post(post: CreatePost, post_id: int, db:Session = Depends(run_db)):
    return blogpostservices.update_post(post, post_id, db)
