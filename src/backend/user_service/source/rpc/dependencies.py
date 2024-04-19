from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from database import engine
from service import UserService
from repo import UserRepo

import redis.asyncio as redis


class UserServiceWrapper:
    async def __aenter__(self):
        self.session = AsyncSession(engine, expire_on_commit=False)
        self.redis = await redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
        return UserService(UserRepo(self.session), self.redis)

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.aclose()
        await self.redis.aclose()
