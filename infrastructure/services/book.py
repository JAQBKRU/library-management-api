from core.repositories.ibook import IBookRepository
from core.domain.book import Book
from typing import List, Iterable


class BookService:
    def __init__(self, repository: IBookRepository):
        self._repository = repository

    async def get_all_books(self) -> Iterable[Book]:
        return await self._repository.get_all_books()

    async def create_book(self, book: Book) -> Book:
        return await self._repository.create_book(book)

    async def update_book(self, book: Book) -> Book:
        return await self._repository.update_book(book)

    async def delete_book(self, book_id: int) -> None:
        await self._repository.delete_book(book_id)
