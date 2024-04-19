from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from fastapi import Depends

from database import get_db
from models import Post

from typing import Sequence


class PostRepo:
    def __init__(self, session: AsyncSession = Depends(get_db)):
        self.session = session

    async def add(self, post_title: str, author_id: int) -> int:
        # Add post to DB, return its ID.

        new_post = Post(title=post_title, author_id=author_id)
        self.session.add(new_post)
        await self.session.flush()

        return new_post.id

    async def delete(self, post_id: int) -> None:
        # Delete post from DB.

        stmt = delete(Post).where(Post.id == post_id)
        await self.session.execute(stmt)

    async def get_all(self) -> Sequence[Post]:
        # Get all posts in DB as a Sequence of Post Models.

        stmt = select(Post)
        result = await self.session.scalars(stmt)
        return result.all()

    async def get_by_id(self, post_id: int) -> Post | None:
        # Get Post Model (or None, if not found) from DB by its id.

        stmt = select(Post).where(Post.id == post_id)
        return await self.session.scalar(stmt)

    async def commit(self) -> None:
        await self.session.commit()
