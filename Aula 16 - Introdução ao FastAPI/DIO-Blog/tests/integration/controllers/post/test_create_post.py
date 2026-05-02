from fastapi import status
from httpx import AsyncClient

async def test_create_post_success(client: AsyncClient, access_token: str):
    # GIVEN
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {
        "title": "Post 1",
        "content": "Content 1",
        "author": "1",
        "published_at": "2022-01-01T00:00:00",
        "published": True
    }
    
    # WHEN
    response = await client.post("posts", json=data, headers=headers)
    
    if response.status_code != 201: # Ou 200, dependendo da sua API
        print(f"\nStatus: {response.status_code}")
        print(f"Corpo da Resposta: {response.text}")

    # THEN
    content = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert content['id'] is not None

async def test_create_post_invalid_payload_fail(client: AsyncClient, access_token: str):
    # GIVEN
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {
        "content": "Content 1",
        "author": "1",
        "published_at": "2022-01-01T00:00:00",
        "published": True
    }
    
    # WHEN
    response = await client.post("posts", json=data, headers=headers)
    
    # THEN
    content = response.json()

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert content['detail'][0]['loc'] == ["body", "title"]

async def test_create_post_not_authenticated_fail(client: AsyncClient):
    # GIVEN
    data = {
        "title": "Post 1",
        "content": "Content 1",
        "author": "1",
        "published_at": "2022-01-01T00:00:00",
        "published": True
    }
    
    # WHEN
    response = await client.post("/posts", json=data, headers={})
    
    # THEN
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
