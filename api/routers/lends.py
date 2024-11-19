from typing import Iterable

from dependency_injector.wiring import inject
from fastapi import APIRouter

from core.domain.lend import BookTransaction

router = APIRouter()

@router.post("/create", response_model=BookTransaction, status_code=201)
@inject
async def create_lend(book_id: int) -> dict:
    pass

@router.get("/all", response_model=Iterable[BookTransaction], status_code=200)
@inject
async def get_all_lend() -> Iterable:
    pass

@router.get("/{lend_id}", response_model=Iterable[BookTransaction], status_code=200)
@inject
async def get_lend_by_id(lend_id: int) -> BookTransaction:
    pass

@router.put("/{lend_id}/", response_model=BookTransaction, status_code=201)
@inject
async def update_lend(lend_id: int) -> dict:
    pass

@router.delete("/{lend_id}/", status_code=204)
@inject
async def delete_lend(lend_id: int) -> None:
    pass