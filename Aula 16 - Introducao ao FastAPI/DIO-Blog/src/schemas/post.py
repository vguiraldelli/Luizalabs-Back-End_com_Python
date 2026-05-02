from datetime import datetime, UTC
from pydantic import BaseModel

class PostIn(BaseModel):
    title: str
    content: str
    author: str
    created_at: datetime = datetime.now(UTC)
    updated_at: datetime = datetime.now(UTC)
    published_at: datetime | None = None
    published: bool = False


class PostUpdateIn(BaseModel):
    title: str | None = None
    content: str | None = None
    author: str | None = None
    updated_at: datetime | None = None
    published_at: datetime | None = None
    published: bool | None = None
   