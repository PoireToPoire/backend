from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: Optional[int] = None
    lastname: str
    firstname: str
    bdate: datetime
    gender: str
    passwd: str
    email: str
    image_path: str
