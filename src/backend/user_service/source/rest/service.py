from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from rest.dependencies import get_db, get_redis
from models import User
from repo import UserRepo
from rest.schemas import UserCredentialsSchema
from service import UserService

import secrets
from redis.asyncio.client import Redis
from fastapi import Depends


class RESTUserService(UserService):
    def __init__(self,
                 session: AsyncSession = Depends(get_db),
                 redis: Redis = Depends(get_redis)):
        self.repo = UserRepo(session)
        self.redis = redis

        super().__init__(self.repo, redis)

    async def authenticate(self, data: UserCredentialsSchema) -> User | None:
        # Verifies user password.

        user = await self.repo.get_by_username(data.username)
        if user is None:
            return None

        if not self.repo.verify_password(user.password, data.password):
            return None

        return user

    async def create_session(self, user_id: int) -> str:
        # Create new session token, add it to Redis and return it.

        session_token = secrets.token_urlsafe()

        await self.redis.set(session_token, user_id, ex=settings.COOKIE_AGE)

        return session_token

    async def delete_session(self, session_token: str) -> None:
        # Delete session token from Redis.

        await self.redis.delete(session_token)
