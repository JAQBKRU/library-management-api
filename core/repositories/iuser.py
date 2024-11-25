from abc import ABC, abstractmethod
from typing import Iterable, Any

from core.domain.user import UserIn, User


class IUserRepository(ABC):
    @abstractmethod
    async def get_all_users(self) -> Iterable[Any]:
        """ Get all users from the repository """

    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> User | None:
        """ Get a user by its ID from the repository """

    @abstractmethod
    async def add_user(self, data: UserIn) -> User | None:
        """ Adds a new user to the repository """

    @abstractmethod
    async def update_user(self, user_id: int, data: UserIn) -> Any | None:
        """ Update an existing user in the repository """

    @abstractmethod
    async def delete_user(self, user_id: int) -> bool:
        """ Remove a user by its ID from the repository """