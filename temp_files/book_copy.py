from pydantic import BaseModel, ConfigDict

class BookCopy(BaseModel):
    id: int
    book_id: int
    is_available: bool