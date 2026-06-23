from pydantic import BaseModel


class PostTags(BaseModel):
    post_id: int 
    tag_id: int