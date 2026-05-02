from database import database
from databases.interfaces import Record
from fastapi import HTTPException
from schemas.post import PostIn, PostUpdateIn
from models.post import posts

class PostService:
    # Ler todos os posts
    async def read_all(self, published: bool | None = None, limit: int = 100, skip: int = 0) -> list[Record]:
        query = posts.select()
        if published is not None:
            query = query.where(posts.c.published == published)
        query = query.limit(limit).offset(skip)
        return await database.fetch_all(query)

    # Ler um post por ID
    async def read(self, id: int) -> Record:
        return await self.__get_by_id(id)

    async def create(self, post: PostIn) -> int:
        command = posts.insert().values(
            title=post.title,
            content=post.content,
            author=post.author,
            published_at=post.published_at,
            published=post.published
        )
        return await database.execute(command)

    # Atualizar um post por ID
    async def update(self, id: int, post: PostUpdateIn) -> Record:
        total = await self.count(id)
        if not total:
            raise HTTPException(status_code=404, detail="Post not found")
        
        data = post.model_dump(exclude_unset=True)
        command = posts.update().where(posts.c.id == id).values(**data)
        await database.execute(command)

        return await self.__get_by_id(id)

    # Deletar um post por ID
    async def delete(self, id: int) -> None:
        command = posts.delete().where(posts.c.id == id)
        await database.execute(command)

    # Contar posts por ID
    async def count(self, id: int) -> int:
        query = "select count(id) as total from posts where id = :id"
        result = await database.fetch_val(query, values={"id": id})
        return result

    # Obter posts por ID
    async def __get_by_id(self, id: int) -> Record:
        query = posts.select().where(posts.c.id == id)
        post = await database.fetch_one(query)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        return post