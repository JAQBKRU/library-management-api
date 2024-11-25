from core.domain.user import UserIn
from core.repositories.iuser import IUserRepository


class UserRepository(IUserRepository):
    async def add_user(self, user: UserIn) -> None:
        """"""

        # query = user_