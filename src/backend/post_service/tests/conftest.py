from asyncio import get_event_loop_policy
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient, ASGITransport

from data import DUMMIES
from models import Post
from database import Base
from main import app
from mock import engine, async_session


@pytest.fixture(autouse=True, scope="session")
def event_loop():
    loop = get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac


@pytest.fixture
async def prepare_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest.fixture
async def create_dummies(prepare_db):
    async with async_session() as session:
        session.add_all(Post(**dummy) for dummy in DUMMIES)
        await session.commit()
