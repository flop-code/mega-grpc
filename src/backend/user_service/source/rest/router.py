from rest.schemas import UserSchema, UserCredentialsSchema
from rest.service import RESTUserService
from rest.exceptions import UnauthorizedError

from config import settings

from fastapi import APIRouter, Depends, Response, Cookie


router = APIRouter()


@router.post("/login")
async def login(response: Response,
                credentials: UserCredentialsSchema,
                user_service: RESTUserService = Depends(RESTUserService)):
    user = await user_service.authenticate(credentials)
    if user is None:
        raise UnauthorizedError("Wrong user credentials.")

    new_session_token = await user_service.create_session(user.id)
    response.set_cookie("session_token", new_session_token, max_age=settings.COOKIE_AGE, **settings.COOKIE_PARAMS)


@router.post("/logout")
async def logout(response: Response,
                 session_token: str | None = Cookie(default=None),
                 user_service: RESTUserService = Depends(RESTUserService)):
    if session_token is not None:
        response.delete_cookie("session_token", **settings.COOKIE_PARAMS)
        await user_service.delete_session(session_token)


@router.get("/current_user")
async def get_current_user(user_service: RESTUserService = Depends(RESTUserService),
                           session_token: str | None = Cookie(default=None)) -> UserSchema:
    if session_token is None:
        raise UnauthorizedError()

    current_user = await user_service.get_current_user(session_token)
    if current_user is None:
        raise UnauthorizedError()

    return UserSchema.model_validate(current_user, from_attributes=True)
