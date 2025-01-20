"""Module providing containers injecting dependencies."""

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Singleton

from src.infrastructure.repositories.itemdb import ItemRepository
from src.infrastructure.services.item import ItemService


class Container(DeclarativeContainer):
    """Container class for dependency injecting purposes."""
    item_repository = Singleton(ItemRepository)

    item_service = Factory(
        ItemService,
        repository=item_repository,
    )
