from datetime import datetime, UTC
from pydantic import BaseModel

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    date: datetime = datetime.now(UTC)
    author: str
    published: bool = False