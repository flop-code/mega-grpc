from argon2.exceptions import VerifyMismatchError

from models import User

from argon2 import PasswordHasher
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession


class UserRepo:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.__hash_manager = PasswordHasher()

    async def get_by_id(self, user_id: int) -> User | None:
        # Get User Model (or None if not found) from DB by its ID.

        stmt = select(User).where(User.id == user_id)
        return await self.session.scalar(stmt)

    async def get_by_username(self, username: str) -> User | None:
        # Get User Model (or None if not found) from DB by its username.

        stmt = select(User).where(User.username == username)
        return await self.session.scalar(stmt)

    def verify_password(self, password_hash: str, password: str) -> bool:
        try:
            self.__hash_manager.verify(password_hash, password)
            return True
        except VerifyMismatchError:
            return False
