from db import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(primary_key=True)
    category_title: Mapped[str] = mapped_column(String(50))
    post: Mapped[list["Post"]] = relationship("Post", back_populates="category")
