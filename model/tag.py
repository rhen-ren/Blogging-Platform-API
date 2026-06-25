from db import Base
from model.posttags import post_tags
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Tag(Base):
    __tablename__ = "tag"
    id: Mapped[int] = mapped_column(primary_key=True)
    tag_title: Mapped[str | None] = mapped_column(String(50))
    posts: Mapped[list["Post"] | None] = relationship(secondary=post_tags, back_populates="tags")