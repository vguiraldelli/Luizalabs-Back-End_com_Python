import asyncio
from httpx import AsyncClient, ASGITransport
from src.main import app

async def main():
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as client:
        res = await client.post('/auth/login', json={'user_id': '1'})
        print('STATUS:', res.status_code)
        print('BODY:', res.json())

if __name__ == '__main__':
    asyncio.run(main())
