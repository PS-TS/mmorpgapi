from typing import Any
from asyncpg import Record  # type: ignore

from src.core.domain.inventory import InventoryIn, Inventory
from src.core.repositories.iinventory import IInventoryRepository
from src.db import inventory_table, database

class InventoryRepository(IInventoryRepository):
    """Klasowe repozytorium do zarządzania pozycjami inventory"""

    async def add_inventory(self, data: InventoryIn) -> Any | None:
        """Dodaje nową pozycję inventory do bazy danych

        Args:
            data (InventoryIn): Atrybuty nowej pozycji inventory

        Returns:
            Any | None: Nowo utworzona pozycja inventory lub None, jeśli operacja się nie powiodła
        """

        query = inventory_table.insert().values(**data.model_dump())
        new_inventory_id = await database.execute(query)
        new_inventory = await self._get_by_id(new_inventory_id)

        return Inventory(**dict(new_inventory)) if new_inventory else None

    async def update_inventory(self, inventory_id: int, data: InventoryIn) -> Any | None:
        """Aktualizuje istniejącą pozycję inventory

        Args:
            inventory_id (int): ID pozycji inventory do zaktualizowania
            data (InventoryIn): Zaktualizowane atrybuty pozycji inventory

        Returns:
            Any | None: Zaktualizowana pozycja inventory lub None, jeśli operacja się nie powiodła
        """

        if await self._get_by_id(inventory_id):
            query = (
                inventory_table.update()
                .where(inventory_table.c.id == inventory_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            inventory = await self._get_by_id(inventory_id)
            return Inventory(**dict(inventory)) if inventory else None

        return None

    async def remove_inventory(self, inventory_id: int) -> bool:
        """Usuwa pozycję inventory z bazy danych

        Args:
            inventory_id (int): ID pozycji inventory do usunięcia

        Returns:
            bool: Powodzenie operacji usuwania
        """

        if await self._get_by_id(inventory_id):
            query = inventory_table.delete().where(inventory_table.c.id == inventory_id)
            await database.execute(query)
            return True

        return False

    async def show_inventory_by_id(self, inventory_id: int) -> Any | None:
        """Pobiera pozycję inventory po jej ID

        Args:
            inventory_id (int): ID pozycji inventory do pobrania

        Returns:
            Any | None: Pozycja inventory, jeśli istnieje, lub None w przeciwnym wypadku
        """

        inventory = await self._get_by_id(inventory_id)
        return Inventory(**dict(inventory)) if inventory else None

    async def _get_by_id(self, inventory_id: int) -> Record | None:
        """Prywatna metoda pobierania pozycji inventory po jej ID

        Args:
            inventory_id (int): ID pozycji inventory

        Returns:
            Record | None: Pozycja inventory, jeśli istnieje, lub None
        """

        query = (
            inventory_table.select()
            .where(inventory_table.c.id == inventory_id)
        )

        return await database.fetch_one(query)
