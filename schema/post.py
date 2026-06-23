from pydantic import BaseModel

class Post(BaseModel):
    post_id: int
    title: str
    content: str
    category_id: int
