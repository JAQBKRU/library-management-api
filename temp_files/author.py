from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class AuthorIn(BaseModel):
    name: str
    biography: Optional[str] = None
    birth_date: Optional[date] = None
    death_date: Optional[date] = None

class Author(AuthorIn):
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")