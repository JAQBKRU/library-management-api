from datetime import date
from typing import List

from pydantic import BaseModel, ConfigDict
from starlette.config import Config

from core.domain.user import User

class UserDTO(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    membership_date: date
    is_active: bool
    borrowed_books: List[int] = []

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        arbitrary_types_allowed=True,
    )