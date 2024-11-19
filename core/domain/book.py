from typing import Optional, List
from pydantic import BaseModel, ConfigDict

class BookIn(BaseModel):
    title: str
    author: str
    epoch: str  # epoch "Pozytywizm"
    has_audio: bool
    genre: str  # genre "Adventure novel"
    kind: str  # type "Epika"
    publication_year: Optional[int] = None
    language: str
    borrowed_count: Optional[int] = 0
    is_available: bool | bool = False

class Book(BookIn):
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")
