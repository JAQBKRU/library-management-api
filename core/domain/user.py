from datetime import date
from typing import List

from pydantic import BaseModel, ConfigDict

class UserIn(BaseModel):
    name: str
    email: str
    phone: str
    membership_date: date
    is_active: bool
    borrowed_books: List[int] = []

class User(UserIn):
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")