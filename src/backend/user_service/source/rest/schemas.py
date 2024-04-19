from abc import ABC

from pydantic import BaseModel, constr, field_validator


class UserBase(BaseModel, ABC):
    username: constr(max_length=25, min_length=5, strip_whitespace=True, to_lower=True)

    @field_validator("username")
    def username_validator(cls, value):
        allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789_"

        if not all(char in allowed_chars for char in value):
            raise ValueError("Wrong username format: Username must only contain letters, numbers, and underscores!")

        return value


class UserCredentialsSchema(UserBase):
    password: constr(max_length=200, min_length=8)

    @field_validator("password")
    def password_validator(cls, value):
        if not any(char.islower() for char in value):
            raise ValueError("Wrong password format: Password must contain at least one lowercase letter!")

        if not any(char.isupper() for char in value):
            raise ValueError("Wrong password format: Password must contain at least one uppercase letter!")

        if not any(char.isdigit() for char in value):
            raise ValueError("Wrong password format: Password must contain at least one digit!")

        return value


class UserSchema(UserBase):
    phone_number: constr(max_length=15, min_length=6)
    address: constr(max_length=425, min_length=12, strip_whitespace=True)

    @field_validator("phone_number")
    def phone_number_validator(cls, value):
        value = "".join(filter(lambda c: c.isdigit(), value.strip()))

        if len(value) < 6:
            raise ValueError("Wrong phone number format: Phone number must be greater than 6 digits!")

        return value

    @field_validator("address")
    def address_validator(cls, value):
        if value.count(", ") != 4:
            raise ValueError("Wrong address format: Address must contain 4 separators (", ")!")
        if not value.split(", ")[-1].isdigit():
            raise ValueError("Wrong address format: Wrong zip code: zip code must be a number!")

        return value
