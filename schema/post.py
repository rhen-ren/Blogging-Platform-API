from pydantic import BaseModel

class CreatePost(BaseModel):
    title: str
    content: str
    category: str
    tags: list[str]

class GetPost(BaseModel):
    id: int
    content: str
    category: str
    category_id: int