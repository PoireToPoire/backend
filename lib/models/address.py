from pydantic import BaseModel


class Address(BaseModel):
    id: int
    user_id: int
    country: str
    state: str
    city: str