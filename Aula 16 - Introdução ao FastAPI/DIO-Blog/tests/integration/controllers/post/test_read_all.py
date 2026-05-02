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

@pytest.mark.parametrize("published,total", [("on", 4), ("off", 2)])
async def test_read_all_posts_by_status_success(client: AsyncClient, access_token: str, published: str, total: int):
    # GIVEN
    params = {"published": published, "limit": 10}
    headers = {"Authorization": f"Bearer {access_token}"}
    
    # WHEN
    response = await client.get(f"/posts/", params=params, headers=headers)
    
    # THEN
    content = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(content) == total

async def test_read_posts_limit_success(client: AsyncClient, access_token: str):
    # GIVEN
    params = {"published": "on", "limit": 1}
    headers = {"Authorization": f"Bearer {access_token}"}
    
    # WHEN
    response = await client.get(f"/posts/", params=params, headers=headers)
    
    # THEN
    content = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(content) == 1

async def test_read_posts_not_authenticated_fail(client: AsyncClient):
    # GIVEN
    params = {"published": "on", "limit": 1}
    
    # WHEN
    response = await client.get("/posts/", params=params, headers={})
    
    # THEN
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

async def test_read_posts_empty_parameters_fail(client: AsyncClient, access_token: str):
    # GIVEN
    headers = {"Authorization": f"Bearer {access_token}"}
    
    # WHEN
    response = await client.get("/posts/", params={}, headers=headers)
    
    # THEN
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
