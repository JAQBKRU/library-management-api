from abc import ABC, abstractmethod
from typing import Iterable
from core.domain.book import Book

class IBookRepository(ABC):
    @abstractmethod
    async def create_book(self, book: Book) -> None:
        """ Adds a new book to the repository """

    @abstractmethod
    async def get_all_books(self) -> Iterable[Book]:
        """ Get all books from the repository """

    @abstractmethod
    async def get_book_by_id(self, book_id: int) -> Book | None:
        """ Get a book by its ID from the repository """

    @abstractmethod
    async def update_book(self, book: Book) -> Book:
        """ Update an existing book in the repository """

    @abstractmethod
    async def delete_book(self, book_id: int) -> None:
        """ Remove a book by its ID from the repository """