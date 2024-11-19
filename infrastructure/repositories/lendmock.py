from typing import Iterable

from core.domain.lend import BookTransaction as Lend
from core.repositories.ilend import ILendRepository
from infrastructure.repositories.db import lends


class LendMockRepository(ILendRepository):
    async def create_lend(self, lend: Lend) -> None:
        lends.append(lend)

    async def get_all_lends(self) -> Iterable[Lend]:
        return lends

    async def get_lend_by_id(self, lend_id: int) -> Lend | None:
        return next((lend for lend in lends if lend.id == lend_id), None)

    async def update_lend(self, lend: Lend) -> Lend:
        pass

    async def delete_lend(self, lend_id: int) -> None:
        lends.remove(lend_id)