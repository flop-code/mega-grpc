from repo import UserRepo
from models import User

from redis import Redis


class UserService:
    def __init__(self, repo: UserRepo, redis: Redis):
        self.repo = repo
        self.redis = redis

    async def get_user_by_id(self, user_id: int) -> User | None:
        return await self.repo.get_by_id(user_id)

    async def get_current_user(self, session_token: str) -> User | None:
        user_id = await self.redis.get(session_token)
        if user_id is None:
            return None

        return await self.get_user_by_id(int(user_id))
