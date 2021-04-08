from pydantic import BaseModel
from datetime import datetime


class FriendList(BaseModel):
    user_id: int
    friend_id: int
