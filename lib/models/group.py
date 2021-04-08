from pydantic import BaseModel


class Group(BaseModel):
    id: int
    owner_id: int 
    category: str
    name: str
