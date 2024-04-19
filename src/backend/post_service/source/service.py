from proto import user_service_pb2

from fastapi import Depends
from google.protobuf.field_mask_pb2 import FieldMask

from exceptions import DeleteForbiddenError, PostNotFoundError
from dependencies import user_service_stub, UserStub
from schemas import UserSchema, PostSchema
from repo import PostRepo


class PostService:
    def __init__(self,
                 repo: PostRepo = Depends(PostRepo),
                 user_service: UserStub = Depends(user_service_stub)):
        self.repo = repo
        self.user_service = user_service

    async def create_post(self, session_token: str, post_title: str) -> int:
        # Create new post, return its ID.

        request = user_service_pb2.UserInfoByTokenRequest(
            user_token=session_token,
            fields=FieldMask(paths=["id"])
        )

        user = await self.user_service.GetUserInfoByToken(request)
        new_post_id = await self.repo.add(post_title, user.id)
        await self.repo.commit()
        return new_post_id

    async def delete_post(self, session_token: str, post_id: int) -> None:
        # Delete post.

        post = await self.repo.get_by_id(post_id)

        if post is None:
            raise PostNotFoundError()

        request = user_service_pb2.UserInfoByTokenRequest(
            user_token=session_token,
            fields=FieldMask(paths=["id"])
        )

        user = await self.user_service.GetUserInfoByToken(request)

        if user.id != post.author_id:
            raise DeleteForbiddenError()

        await self.repo.delete(post_id)
        await self.repo.commit()

    async def get_all_posts(self) -> list[PostSchema]:
        # Get all posts as a list of Post Schemas.

        posts = await self.repo.get_all()

        return [
            PostSchema.model_validate(post, from_attributes=True)
            for post in posts
        ]

    async def get_post_author(self, post_id: int) -> UserSchema:
        # Get author of the post as a User Schema.

        post = await self.repo.get_by_id(post_id)

        if post is None:
            raise PostNotFoundError()

        request = user_service_pb2.UserInfoByIdRequest(
            user_id=post.author_id,
            fields=FieldMask(paths=["username", "phone_number", "address"])
        )

        user = await self.user_service.GetUserInfoById(request)

        return UserSchema.model_validate(user, from_attributes=True)
