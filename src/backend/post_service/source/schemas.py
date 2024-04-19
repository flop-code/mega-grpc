from pydantic import BaseModel, conint


class UserSchema(BaseModel):
    username: str
    phone_number: str
    address: str


class PostTitle(BaseModel):
    title: str


class PostSchema(PostTitle):
    id: conint(gt=0, le=2147483647)
