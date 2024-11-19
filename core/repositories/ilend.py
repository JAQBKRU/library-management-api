from abc import ABC, abstractmethod
from typing import Iterable
from core.domain.lend import BookTransaction as Lend

class ILendRepository(ABC):
    @abstractmethod
    async def create_lend(self, lend: Lend) -> None:
        """ Adds a new lend to the repository """

    @abstractmethod
    async def get_all_lends(self) -> Iterable[Lend]:
        """ Get all lends from the repository """

    @abstractmethod
    async def get_lend_by_id(self, lend_id: int) -> Lend | None:
        """ Get lend by its ID from the repository """

    @abstractmethod
    async def update_lend(self, lend: Lend) -> Lend:
        """ Update an existing lend in the repository """

    @abstractmethod
    async def delete_lend(self, lend_id: int) -> None:
        """ Remove lend by its ID from the repository """