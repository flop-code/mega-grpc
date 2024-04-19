from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from database import async_session
import redis.asyncio as redis


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


async def get_redis() -> AsyncGenerator[redis.Redis, None]:
    async with redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT) as connection:
        yield connection
