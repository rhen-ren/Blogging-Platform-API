from pydantic import BaseModel

class tag(BaseModel):
    tag_id: int
    tag_title: str