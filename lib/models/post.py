from pydantic import BaseModel
from typing import Optional


class Post(BaseModel):
    id: int
    user_id: int
    parent_post_id: Optional[int]
    title: str
    content: str
    category: str
    type: bool