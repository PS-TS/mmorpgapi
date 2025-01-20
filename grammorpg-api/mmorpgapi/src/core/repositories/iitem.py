"""Module containing item repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable

from src.core.domain.item import ItemIn


class IItemRepository(ABC):
    """An abstract class representing protocol of item repository."""

    @abstractmethod
    async def get_item_by_id(self, item_id: int) -> Any | None:
        """The abstract getting an item from the data storage.

        Args:
            item_id (int): The id of the item.

        Returns:
            Any | None: The item data if exists.
        """

    @abstractmethod
    async def get_all_items(self) -> Iterable[Any]:
        """The abstract getting all items from the data storage.

        Returns:
            Iterable[Any]: The collection of all items.
        """

    @abstractmethod
    async def get_item_by_name(self, name: str) -> Any | None:
        """The abstract getting an item by name from the data storage.

        Args:
            name (str): The name of the item.

        Returns:
            Any | None: The item data if exists.
        """

    @abstractmethod
    async def add_item(self, data: ItemIn) -> Any | None:
        """The abstract adding a new item to the data storage.

        Args:
            data (ItemIn): The attributes of the item.

        Returns:
            Any | None: The newly created item.
        """

    @abstractmethod
    async def update_item(self, item_id: int, data: ItemIn) -> Any | None:
        """The abstract updating item data in the data storage.

        Args:
            item_id (int): The item id.
            data (ItemIn): The attributes of the item.

        Returns:
            Any | None: The updated item.
        """

    @abstractmethod
    async def delete_item(self, item_id: int) -> bool:
        """The abstract removing an item from the data storage.

        Args:
            item_id (int): The item id.

        Returns:
            bool: Success of the operation.
        """
