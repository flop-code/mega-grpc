from database import Base

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column


class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int]             = mapped_column(primary_key=True)
    title: Mapped[str]          = mapped_column(String(125), nullable=False)
    author_id: Mapped[int]      = mapped_column(Integer, nullable=False)
