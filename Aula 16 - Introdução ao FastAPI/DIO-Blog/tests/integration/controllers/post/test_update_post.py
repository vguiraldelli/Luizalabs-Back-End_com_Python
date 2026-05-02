import pytest
import pytest_asyncio
from fastapi import status
from httpx import AsyncClient


@pytest_asyncio.fixture(autouse=True)
async def populate_posts(db):
    from schemas.post import PostIn
    from services.post import PostService

    service = PostService()
    await service.create(PostIn(title="Post 1", content="Content 1", author="1", published=True))
    await service.create(PostIn(title="Post 2", content="Content 2", author="1", published=True))
    await service.create(PostIn(title="Post 3", content="Content 3", author="1", published=False))
    await service.create(PostIn(title="Post 4", content="Content 4", author="1", published=True))
    await service.create(PostIn(title="Post 5", content="Content 5", author="1", published=False))
    await service.create(PostIn(title="Post 6", content="Content 6", author="1", published=True))

async def test_update_post_success(client: AsyncClient, access_token: str):
    # GIVEN
    headers = {"Authorization": f"Bearer {access_token}"}
    post_id = 1
    data = {
        "title": "Updated Post 1",
        "content": "Updated Content 1",
        "author": "1",
        "published_at": "2022-01-01T00:00:00",
        "published": True
    }
    
    # WHEN
    response = await client.put(f"/posts/{post_id}", json=data, headers=headers)
    
    # THEN
    content = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert content['title'] == data["title"]

async def test_update_post_not_authenticated_fail(client: AsyncClient):
    # GIVEN
    post_id = 1
    
    # WHEN
    response = await client.put(f"/posts/{post_id}", headers={})
    
    # THEN
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

async def test_update_post_not_found_fail(client: AsyncClient, access_token: str):
    # GIVEN
    headers = {"Authorization": f"Bearer {access_token}"}
    post_id = 652
    data = {
        "title": "Updated Post 1",
        "content": "Updated Content 1",
        "author": "1",
        "published_at": "2022-01-01T00:00:00",
        "published": True
    }
    
    # WHEN
    response = await client.put(f"/posts/{post_id}", json=data, headers=headers)
    
    # THEN

    assert response.status_code == status.HTTP_404_NOT_FOUND
