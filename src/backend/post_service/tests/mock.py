from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from data import test_settings
from database import Base, get_db
from main import app

engine = create_async_engine(url=test_settings.dsn)
Base.metadata.bind = engine
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


async def override_get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


app.dependency_overrides[get_db] = override_get_db
