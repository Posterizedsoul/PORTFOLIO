from datetime import datetime
from typing import List

from pydantic import BaseModel


class BlogPost(BaseModel):
    title: str
    content: str
    date: datetime
    tags: List[str]
    is_published: bool
    summary: str

