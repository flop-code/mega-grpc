from typing import AsyncGenerator

import redis.asyncio as redis
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from data import test_settings
from database import Base
from rest.dependencies import get_db, get_redis
from rest.main import app

engine = create_async_engine(url=test_settings.dsn)
Base.metadata.bind = engine
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


async def override_get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


async def override_get_redis() -> AsyncGenerator[redis.Redis, None]:
    async with redis.from_url("redis://" + test_settings.TEST_REDIS_HOST) as connection:
        yield connection


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_redis] = override_get_redis
