from pydantic import BaseModel

class Category(BaseModel):
    category_id: int
    category_title: str