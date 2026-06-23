from fastapi import FastAPI, APIRouter
from schema.post import Post
from testData import testData

router = APIRouter(prefix="/blogpost")


@router.get("/posts")
def get_posts() -> Post:
    return testData

