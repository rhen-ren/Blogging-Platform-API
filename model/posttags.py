from db import Base
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey

post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", ForeignKey("post.id"), primary_key=True),
    Column("tag_id", ForeignKey("tag.id"), primary_key=True)
)
