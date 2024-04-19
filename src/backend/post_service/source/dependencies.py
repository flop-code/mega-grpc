from proto.user_service_pb2_grpc import UserStub
from typing import AsyncGenerator
from config import settings
import grpc


async def user_service_stub() -> AsyncGenerator[UserStub, None]:
    user_service_url = f"{settings.USER_SERVICE_HOST}:{settings.USER_SERVICE_PORT}"
    async with grpc.aio.insecure_channel(user_service_url) as channel:
        stub = UserStub(channel)
        yield stub
