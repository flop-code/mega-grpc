import pytest

from data import DUMMIES, PASSWORD
from httpx import AsyncClient


@pytest.mark.parametrize("user", DUMMIES)
async def test_login_success(ac: AsyncClient, user: dict[str], create_dummies):
    response = await ac.post("/login", json={"username": user["username"], "password": PASSWORD})
    assert response.status_code == 200
    assert response.cookies.jar


@pytest.mark.parametrize("data, code", [
    ({"username": "dummy1"}, 422),
    ({"username": "dummy2", "password": "helloWORLD345"}, 401),
    ({"username": "dummy3", "password": "helloworld345"}, 422)
])
async def test_login_fail(ac: AsyncClient, data: dict[str], code: int, create_dummies):
    response = await ac.post("/login", json=data)
    assert response.status_code == code


async def test_logout(ac: AsyncClient, create_dummies):
    response = await ac.post("/logout")
    assert not response.headers.get_list("Set-Cookie")
    assert not response.cookies.jar


async def test_get_current_user(ac: AsyncClient, create_dummies):
    response = await ac.get("/current_user")
    assert response.status_code == 401
    assert response.json() == {"detail": "Not logged in."}

