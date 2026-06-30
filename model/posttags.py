from db import Base
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class PostTags(Base):
    __tablename__ = "post_tags"
    post_id: Mapped[int] = mapped_column("post_id", ForeignKey("post.id"), primary_key=True)
    tag_id: Mapped[int] = mapped_column("tag_id", ForeignKey("tag.id"), primary_key=True)
