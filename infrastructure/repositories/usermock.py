from typing import Iterable

from core.domain.user import User
from core.repositories.iuser import IUserRepository
from infrastructure.repositories.db import users


class UserMockRepository(IUserRepository):
    async def get_all_users(self) -> Iterable[User]:
        return users

    async def get_user_by_id(self, user_id: int) -> User | None:
        return next((user for user in users if user.id == user_id), None)

    async def add_user(self, user: User) -> None:
        users.append(user)

    async def update_user(self, user: User) -> User:
        pass

    async def delete_user(self, user_id: int) -> None:
        users.remove(user_id)
