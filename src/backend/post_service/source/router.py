from fastapi import APIRouter, Depends, Cookie
from pydantic import conint
from typing_extensions import TypedDict

from exceptions import UnauthorizedError
from schemas import UserSchema, PostSchema, PostTitle
from service import PostService

router = APIRouter()


@router.post("/create")
async def create_post(title: PostTitle,
                      session_token: str | None = Cookie(default=None),
                      post_service: PostService = Depends(PostService)) -> \
        TypedDict("PostID", {"id": int}):
    if session_token is None:
        raise UnauthorizedError()

    new_post_id = await post_service.create_post(session_token, title.title)
    return {"id": new_post_id}


@router.delete("/{post_id}")
async def delete_post(post_id: conint(gt=0, le=2147483647),
                      session_token: str | None = Cookie(default=None),
                      post_service: PostService = Depends(PostService)):
    if session_token is None:
        raise UnauthorizedError()

    await post_service.delete_post(session_token, post_id)


@router.get("/all")
async def get_all(post_service: PostService = Depends(PostService)) -> \
        TypedDict("All posts", {"posts": list[PostSchema]}):
    posts = await post_service.get_all_posts()
    return {"posts": posts}


@router.get("/{post_id}")
async def get_post_author(post_id: conint(gt=0, le=2147483647),
                          post_service: PostService = Depends(PostService)) -> UserSchema:
    return await post_service.get_post_author(post_id)
