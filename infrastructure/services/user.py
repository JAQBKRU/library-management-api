from abc import ABC, abstractmethod
from typing import Iterable

from core.domain.user import User, UserIn


class IUserService(ABC):
    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> User | None:
        """
        """