from fastapi import HTTPException
from views.post import PostOut
from schemas.post import PostIn, PostUpdateIn
from typing import Annotated
from fastapi import FastAPI, APIRouter, status, Cookie, Header, Response, Depends
from datetime import datetime, UTC
from models.post import posts
from database import database
from services.post import PostService
from controllers.security import login_required

service = PostService()

router = APIRouter(prefix="/posts", tags=["posts"], dependencies=[Depends(login_required)])

# fake_db = [
#     {"title": "Post 1", "content": "Content 1", "author": "Author 1", 'published': True},
#     {"title": "Post 2", "content": "Content 2", "author": "Author 2", 'published': True},
#     {"title": "Post 3", "content": "Content 3", "author": "Author 3", 'published': False}
# ]

# Listar todos os posts
@router.get("/", response_model=list[PostOut])
async def read_all_posts(published: bool | None = None, limit: int = 100, skip: int = 0):
    return await service.read_all(published=published, limit=limit, skip=skip)

# Ler um post por id
@router.get("/{id}", response_model=PostOut)
async def read_post(id: int):
    return await service.read(id)

# Criar um novo post
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(post: PostIn):
    command = posts.insert().values(
        title=post.title,
        content=post.content,
        author=post.author,
        published_at=post.published_at,
        published=post.published
    )
    last_record_id = await database.execute(command)
    return {**post.model_dump(), "id": last_record_id}

# Atualizar um post
@router.patch("/{id}", response_model=PostOut)
async def update_post(id: int, post: PostUpdateIn):
    return await service.update(id, post)    

# Deletar um post
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_post(id: int):
    return await service.delete(id)

# Exemplo de como ler posts por framework
@router.get("/framework/{framework}", response_model=list[PostOut])
def read_frameworkposts(framework: str):
    return [{
            'title': 'Criando uma aplicação com ' + framework, 'date': datetime.now(UTC),
            'title': f'Internacionalizando uma aplicação com {framework}', 'date': datetime.now(UTC),
            'title': f'Testes de uma aplicação com {framework}', 'date': datetime.now(UTC)
        }]



