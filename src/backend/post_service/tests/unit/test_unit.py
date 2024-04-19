from httpx import AsyncClient


async def test_get_all_posts(ac: AsyncClient, create_dummies):
    response = await ac.get("/all")
    assert response.status_code == 200
    assert response.json() == {
        "posts": [
            {"title": "Hello world!", "id": 1},
            {"title": "Hello again.", "id": 2},
            {"title": "Another author!", "id": 3}
        ]
    }
