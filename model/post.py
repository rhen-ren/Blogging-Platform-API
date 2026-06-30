import datetime
from db import Base
from model.posttags import PostTags
from model.category import Category
from model.tag import Tag
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    content: Mapped[str] = mapped_column(String(200))
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    category: Mapped["Category"] = relationship("Category", back_populates="post")
    post_tags: Mapped["PostTags"] = relationship("PostTags", back_populates= "post")
    createdAt: Mapped["datetime"] = mapped_column(DateTime, default=func.now())
    updatedAt: Mapped["datetime"] = mapped_column(DateTime, default=func.now(), onupdate=func.now())