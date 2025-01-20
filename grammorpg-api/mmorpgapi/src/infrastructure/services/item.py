"""Module containing item service implementation."""

from typing import Iterable

from src.core.domain.item import Item, ItemIn
from src.core.repositories.iitem import IItemRepository
from src.infrastructure.services.iitem import IItemService


class ItemService(IItemService):
    """A class implementing the item service."""

    _repository: IItemRepository

    def __init__(self, repository: IItemRepository) -> None:
        """The initializer of the `item service`.

        Args:
            repository (IItemRepository): The reference to the repository.
        """

        self._repository = repository

    async def get_item_by_id(self, item_id: int) -> Item | None:
        """The method getting an item from the repository.

        Args:
            item_id (int): The id of the item.

        Returns:
            Item | None: The item data if exists.
        """

        return await self._repository.get_item_by_id(item_id)

    async def get_all_items(self) -> Iterable[Item]:
        """The method getting all items from the repository.

        Returns:
            Iterable[Item]: The collection of all items.
        """

        return await self._repository.get_all_items()

    async def add_item(self, data: ItemIn) -> Item | None:
        """The method adding a new item to the repository.

        Args:
            data (ItemIn): The attributes of the item.

        Returns:
            Item | None: The newly created item.
        """

        return await self._repository.add_item(data)

    async def update_item(self, item_id: int, data: ItemIn) -> Item | None:
        """The method updating item data in the repository.

        Args:
            item_id (int): The item id.
            data (ItemIn): The attributes of the item.

        Returns:
            Item | None: The updated item.
        """

        return await self._repository.update_item(
            item_id=item_id,
            data=data,
        )

    async def delete_item(self, item_id: int) -> bool:
        """The method removing an item from the repository.

        Args:
            item_id (int): The item id.

        Returns:
            bool: Success of the operation.
        """

        return await self._repository.delete_item(item_id)
