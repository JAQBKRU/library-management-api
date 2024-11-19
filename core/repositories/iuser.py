from abc import ABC, abstractmethod
from typing import Iterable
from core.domain.user import User

class IUserRepository(ABC):
    @abstractmethod
    async def get_all_users(self) -> Iterable[User]:
        """ Get all users from the repository """

    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> User | None:
        """ Get a user by its ID from the repository """

    @abstractmethod
    async def add_user(self, user: User) -> None:
        """ Adds a new user to the repository """

    @abstractmethod
    async def update_user(self, user: User) -> User:
        """ Update an existing user in the repository """

    @abstractmethod
    async def delete_user(self, user_id: int) -> None:
        """ Remove a user by its ID from the repository """