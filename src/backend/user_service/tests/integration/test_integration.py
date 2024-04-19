import pytest
from data import DUMMIES, PASSWORD
from httpx import AsyncClient


@pytest.mark.parametrize("user", DUMMIES)
async def test_login_logout(ac: AsyncClient, user: dict[str], create_dummies):
    login_response = await ac.post("/login", json={"username": user["username"], "password": PASSWORD})
    ac.cookies = login_response.cookies
    logout_response = await ac.post("/logout")

    assert logout_response.status_code == 200
    assert not logout_response.cookies.jar


@pytest.mark.parametrize("user", DUMMIES)
async def test_login_get(ac: AsyncClient, user: dict[str], create_dummies):
    login_response = await ac.post("/login", json={"username": user["username"], "password": PASSWORD})
    ac.cookies = login_response.cookies

    current_user_response = await ac.get("/current_user")
    assert current_user_response.status_code == 200
    assert current_user_response.json() == user


@pytest.mark.parametrize("user", [
    {"username": "dummy1", "password": "helloWORLD1234"},
    {"username": "dummy2", "password": "helloWORLD345"},
    {"username": "dummy69", "password": "helloWORLD123"}
])
async def test_login_get_failed(ac: AsyncClient, user: dict[str], create_dummies):
    login_response = await ac.post("/login", json={"username": user["username"], "password": user["password"]})
    ac.cookies = login_response.cookies

    current_user_response = await ac.get("/current_user")
    assert current_user_response.status_code == 401
    assert current_user_response.json() == {"detail": "Not logged in."}


@pytest.mark.parametrize("user", DUMMIES)
async def test_login_get_logout_get(ac: AsyncClient, user: dict[str], create_dummies):
    login_response = await ac.post("/login", json={"username": user["username"], "password": PASSWORD})
    ac.cookies = login_response.cookies

    await ac.get("/current_user")

    logout_response = await ac.post("/logout")
    ac.cookies = logout_response.cookies

    get_logged_out_user_response = await ac.get("/current_user")
    assert get_logged_out_user_response.status_code == 401
    assert get_logged_out_user_response.json() == {"detail": "Not logged in."}
