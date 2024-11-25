from abc import ABC, abstractmethod
from typing import Iterable

from core.domain.user import User, UserIn


class IUserService(ABC):
    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> User | None:
        """"""

    @abstractmethod
    async def get_all(self) -> Iterable[UserIn]:
        """"""

    @abstractmethod
    async def add_user(self, data: UserIn) -> User | None:
        """"""

    @abstractmethod
    async def update_user(
            self,
            user_id: int,
            data: UserIn,
    ) -> UserIn | None:
        """"""

    @abstractmethod
    async def delete_user(self, user_id: int) -> bool:
        """"""