from pydantic import BaseModel, ConfigDict
from datetime import date

class BookTransaction(BaseModel):
    id: int
    user_id: int
    book_id: int
    loan_date: date
    return_date: date = None
    is_returned: bool = False