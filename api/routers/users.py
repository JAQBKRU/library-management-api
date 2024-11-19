from typing import Iterable

from dependency_injector.wiring import inject, Provide
from fastapi import Depends, APIRouter

from core.domain.user import User, UserIn

router = APIRouter()

@router.post("/create", response_model=User, status_code=201)
@inject
async def create_user(user: UserIn) -> dict:
    pass

@router.get("/all", response_model=Iterable[User], status_code=200)
@inject
async def get_all_user() -> Iterable:
    pass

@router.get("/{user_id}", response_model=Iterable[User], status_code=200)
@inject
async def get_user_by_id(user_id: int) -> User:
    pass

@router.put("/{user_id}/", response_model=User, status_code=201)
@inject
async def update_user(user_id: int) -> dict:
    pass

@router.delete("/{user_id}/", status_code=204)
@inject
async def delete_user(user_id: int) -> None:
    pass