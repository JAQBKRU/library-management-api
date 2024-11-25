from typing import Iterable

from core.repositories.iuser import IUserRepository
from core.domain.user import User, UserIn
from infrastructure.repositories.db import users


class UserMockRepository(IUserRepository):
    async def get_all_users(self) -> Iterable[User]:
        return users

    async def get_user_by_id(self, user_id: int) -> User | None:
        return next((user for user in users if user.id == user_id), None)

    # async def add_user(self, data: UserIn) -> None:
        # users.append(data)
    async def add_user(self, data: UserIn) -> User | None:
        new_user = User(
            id=len(users) + 1,
            name=data.name,
            email=data.email,
            phone=data.phone,
            membership_date=data.membership_date,
            is_active=True
        )
        users.append(new_user)
        return new_user

    async def update_user(
            self,
            user_id: int,
            data: UserIn
    ) -> UserIn | None:
        if user_pos := next((i for i, x in enumerate(users) if x.id == user_id), None):
            users[user_pos] = User(id=user_id, **data.model_dump())
            return users[user_pos]
        return None

    async def delete_user(self, user_id: int) -> bool:
        if user_pos := next(filter(lambda x: x.id == user_id, users)):
            users.remove(user_pos)
            return True
        return False
