from pydantic import BaseModel
from datetime import datetime

class CreatePost(BaseModel):
    title: str
    content: str
    category: str
    tags: list[str]

class GetPost(BaseModel):
    id: int
    title: str
    content: str
    category: str
    tags: list[str]
    createdAt: datetime
    updatedAt: datetime