"""Module containing item service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable

from src.core.domain.item import Item, ItemIn


class IItemService(ABC):
    """An abstract class representing protocol of item service."""

    @abstractmethod
    async def get_item_by_id(self, item_id: int) -> Item | None:
        """The abstract getting an item from the repository.

        Args:
            item_id (int): The id of the item.

        Returns:
            Item | None: The item data if exists.
        """

    @abstractmethod
    async def get_all_items(self) -> Iterable[Item]:
        """The abstract getting all items from the repository.

        Returns:
            Iterable[Item]: The collection of all items.
        """

    @abstractmethod
    async def add_item(self, data: ItemIn) -> Item | None:
        """The abstract adding new item to the repository.

        Args:
            data (ItemIn): The attributes of the item.

        Returns:
            Item | None: The newly created item.
        """

    @abstractmethod
    async def update_item(self, item_id: int, data: ItemIn) -> Item | None:
        """The abstract updating item data in the repository.

        Args:
            item_id (int): The item id.
            data (ItemIn): The attributes of the item.

        Returns:
            Item | None: The updated item.
        """

    @abstractmethod
    async def delete_item(self, item_id: int) -> bool:
        """The abstract removing item from the repository.

        Args:
            item_id (int): The item id.

        Returns:
            bool: Success of the operation.
        """
