from pydantic import BaseModel
from datetime import datetime


class Event(BaseModel):
    id: int
    user_id: int
    adresse: int
    date: datetime