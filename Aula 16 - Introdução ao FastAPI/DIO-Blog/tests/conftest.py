import os
import asyncio
import pytest_asyncio
from httpx import ASGITransport, AsyncClient


# Rodar os testes:
# -> poetry run pytest -v
# -> poetry run pytest -v -s tests/integration/controllers/auth/test_login.py
# -> poetry run pytest -v tests/integration/controllers/post/test_create_post.py
# -> poetry run pytest -v tests/integration/controllers/post/test_read_all.py
# -> poetry run pytest -v tests/integration/controllers/post/test_update_post.py
# -> poetry run pytest -v tests/integration/controllers/post/test_delet_post.py

os.environ.setdefault("DATABASE_URL", f"sqlite:///../tests.db") # noqa

@pytest_asyncio.fixture
async def db(request):
    from database import database, engine, metadata #noqa
    from models.post import posts #noqa

    await database.connect()
    metadata.create_all(engine)
    
    def teardown():
        async def _teardown():
            await database.disconnect()
            metadata.drop_all(engine)            
        asyncio.run(_teardown())
    request.addfinalizer(teardown)


@pytest_asyncio.fixture
async def client(db):
    from main import app
    transport = ASGITransport(app=app)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    async with AsyncClient(
        base_url="http://test",
        transport=transport,
        headers=headers,
        follow_redirects=True
    ) as client:
        yield client
        
@pytest_asyncio.fixture
async def access_token(client):
    response = await client.post("auth/login", json={"user_id": "1"})
    return response.json()["access_token"]
