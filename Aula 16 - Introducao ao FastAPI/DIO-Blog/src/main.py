from typing import Annotated
from fastapi import FastAPI, status, Cookie, Header, Response
from contextlib import asynccontextmanager
from pydantic import BaseModel
from database import database, metadata, engine
from controllers import post
from controllers import auth

# Colocar a API no ar com o comando:
# -> poetry run uvicorn main:app --reload --app-dir src
# Testar no navegador com: http://[IP_ADDRESS]/posts/flask
# http://[IP_ADDRESS]/docs para acessar o swagger
# http://127.0.0.1:8000/posts


@asynccontextmanager
async def lifespan(app: FastAPI):
    from models.post import posts # noqa: F401

    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(post.router)
app.include_router(auth.router)


# Testes
@app.get("/")
def read_root():
    return {"message": "Hello World!!!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


# Exemplo de retorno de dados em formato JSON
class Foo(BaseModel):
    bar: str
    message: str

@app.get("/foobar/", response_model=Foo)
def foobar() -> dict[str, str]:
    return {"bar": "foo", "message": "Hello World!!!"}