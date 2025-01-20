"""Module containing item database repository implementation."""

from typing import Any, Iterable

from asyncpg import Record  # type: ignore

from src.core.domain.item import Item, ItemIn
from src.core.repositories.iitem import IItemRepository
from src.db import item_table, database


class ItemRepository(IItemRepository):
    """A class implementing the item repository."""

    async def get_item_by_id(self, item_id: int) -> Any | None:
        """The method getting an item from the data storage.

        Args:
            item_id (int): The id of the item.

        Returns:
            Any | None: The item data if exists.
        """

        item = await self._get_by_id(item_id)

        return Item(**dict(item)) if item else None

    async def get_all_items(self) -> Iterable[Any]:
        """The method getting all items from the data storage.

        Returns:
            Iterable[Any]: The collection of all items.
        """

        query = item_table.select().order_by(item_table.c.name.asc())
        items = await database.fetch_all(query)

        return [Item(**dict(item)) for item in items]

    async def get_item_by_name(self, name: str) -> Any | None:
        """The method getting an item by name from the data storage.

        Args:
            name (str): The name of the item.

        Returns:
            Any | None: The item data if exists.
        """

        query = (
            item_table.select()
            .where(item_table.c.name == name)
            .order_by(item_table.c.name.asc())
        )
        item = await database.fetch_one(query)

        return Item(**dict(item)) if item else None

    async def add_item(self, data: ItemIn) -> Any | None:
        """The method adding a new item to the data storage.

        Args:
            data (ItemIn): The attributes of the item.

        Returns:
            Any | None: The newly created item.
        """

        query = item_table.insert().values(**data.model_dump())
        new_item_id = await database.execute(query)
        new_item = await self._get_by_id(new_item_id)

        return Item(**dict(new_item)) if new_item else None

    async def update_item(self, item_id: int, data: ItemIn) -> Any | None:
        """The method updating item data in the data storage.

        Args:
            item_id (int): The item id.
            data (ItemIn): The attributes of the item.

        Returns:
            Any | None: The updated item.
        """

        if self._get_by_id(item_id):
            query = (
                item_table.update()
                .where(item_table.c.id == item_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            item = await self._get_by_id(item_id)

            return Item(**dict(item)) if item else None

        return None

    async def delete_item(self, item_id: int) -> bool:
        """The method removing an item from the data storage.

        Args:
            item_id (int): The item id.

        Returns:
            bool: Success of the operation.
        """

        if self._get_by_id(item_id):
            query = item_table.delete().where(item_table.c.id == item_id)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, item_id: int) -> Record | None:
        """A private method getting an item from the DB based on its ID.

        Args:
            item_id (int): The ID of the item.

        Returns:
            Any | None: Item record if exists.
        """

        query = (
            item_table.select()
            .where(item_table.c.id == item_id)
            .order_by(item_table.c.name.asc())
        )

        return await database.fetch_one(query)
