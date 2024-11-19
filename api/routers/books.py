from typing import List, Iterable

from dependency_injector.wiring import inject
from fastapi import APIRouter, HTTPException

from core.domain.book import Book, BookIn
from infrastructure.services.book import BookService

router = APIRouter()

book_service = BookService(...)

@router.post("/create", response_model=Book, status_code=200)
@inject
async def create_book(book: Book):
    return book_service.create_book(book)

@router.get("/books", response_model=List[Book], status_code=201)
@inject
async def get_books():
    return book_service.get_all_books()

@router.get("/{book_id}", response_model=Iterable[Book], status_code=200)
@inject
async def get_book_by_id(book_id: int) -> Book:
    pass

@router.put("/{book_id}", response_model=Book, status_code=200)
@inject
async def update_book(book_id: int, book: Book):
    return book_service.update_book(book)

@router.delete("/books/{book_id}", status_code=204)
@inject
async def delete_book(book_id: int):
    await book_service.delete_book(book_id)
    return {"message": "Book deleted successfully."}