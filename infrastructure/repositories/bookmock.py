from typing import Iterable

from core.domain.book import Book
from core.repositories.ibook import IBookRepository
from infrastructure.repositories.db import books


class BookMockRepository(IBookRepository):
    async def create_book(self, book: Book) -> None:
        books.append(book)

    async def get_all_books(self) -> Iterable[Book]:
        return books

    async def get_book_by_id(self, book_id: int) -> Book | None:
        return next((book for book in books if book.id == book_id), None)

    async def update_book(self, book: Book) -> Book:
        pass

    async def delete_book(self, book_id: int) -> None:
        books.remove(book_id)