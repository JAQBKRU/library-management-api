from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Singleton

# from infrastructure.repositories.userdb import UserRepository
from infrastructure.repositories.usermock import UserMockRepository

from infrastructure.services.user import UserService


class Container(DeclarativeContainer):
    user_repository = Singleton(UserMockRepository)
    # user_repository = Singleton(UserRepository)

    user_service = Factory(
        UserService,
        repository=user_repository,
    )