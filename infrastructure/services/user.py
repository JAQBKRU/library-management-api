from typing import Iterable

from core.domain.user import UserIn, User
from core.repositories.iuser import IUserRepository
from infrastructure.services.iuser import IUserService


class UserService(IUserService):
    _repository: IUserRepository

    def __init__(self, repository: IUserRepository) -> None:
        self._repository = repository

    async def add_user(self, data: UserIn) -> User | None:
        return await self._repository.add_user(data)

    async def get_all(self) -> Iterable[UserIn]:
        return await self._repository.get_all_users()

    async def get_user_by_id(self, user_id: int) -> User | None:
        return await self._repository.get_user_by_id(user_id)

    async def update_user(
            self,
            user_id: int,
            data: UserIn,
    ) -> UserIn | None:
        return await self._repository.update_user(
            user_id=user_id,
            data=data,
        )

    async def delete_user(self, user_id: int) -> bool:
        return await self._repository.delete_user(user_id)