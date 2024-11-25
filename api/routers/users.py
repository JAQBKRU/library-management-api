from typing import Iterable

from dependency_injector.wiring import inject, Provide
from fastapi import Depends, APIRouter, HTTPException

from container import Container
from core.domain.user import User, UserIn

from infrastructure.services.iuser import IUserService

router = APIRouter()

@router.post("/create", response_model=User, status_code=201)
@inject
async def create_user(
        user: UserIn,
        service: IUserService = Depends(Provide[Container.user_service])
    ) -> dict:

    # new_user = await service.add_user(user)
    # return new_user.model_dump() if new_user else {}
    new_user = await service.add_user(user)
    return {**user.model_dump(), "id": 0}

@router.get("/all", response_model=list[User], status_code=200)
@inject
async def get_all_users(
        service: IUserService = Depends(Provide[Container.user_service]),
) -> list:#-> Iterable

    users = await service.get_all()
    # return users
    return [{**user.model_dump()}
            for i, user in enumerate(users)]

@router.get("/{user_id}", response_model=User, status_code=200)
@inject
async def get_user_by_id(
        user_id: int,
        service: IUserService = Depends(Provide[Container.user_service]),
) -> dict | None:
    if user := await service.get_user_by_id(user_id):
        return {**user.model_dump(), "id": user_id}

    raise HTTPException(status_code=404, detail="User not found")

@router.put("/{user_id}/", response_model=User, status_code=201)
@inject
async def update_user(
        user_id: int,
        updated_user: UserIn,
        service: IUserService = Depends(Provide[Container.user_service])
) -> dict:
    if await service.get_user_by_id(user_id=user_id):
        await service.update_user(
            user_id=user_id,
            data=updated_user,
        )
        return {**updated_user.model_dump(), "id": user_id}

    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}/", status_code=204)
@inject
async def delete_user(
        user_id: int,
        service: IUserService = Depends(Provide[Container.user_service]),
) -> None:
    if await service.get_user_by_id(user_id=user_id):
        await service.delete_user(user_id)

        return

    raise HTTPException(status_code=404, detail="User not found")