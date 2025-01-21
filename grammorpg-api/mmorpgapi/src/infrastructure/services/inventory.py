from typing import Iterable

from src.core.domain.inventory import Inventory, InventoryIn
from src.core.repositories.iinventory import IInventoryRepository
from src.infrastructure.services.iinventory import IInventoryService


class InventoryService(IInventoryService):
    """Klasa implementująca serwis dla inventory."""

    _repository: IInventoryRepository

    def __init__(self, repository: IInventoryRepository) -> None:
        """Inicjalizator serwisu inventory.

        Args:
            repository (IInventoryRepository): Referencja do repozytorium.
        """
        self._repository = repository

    async def get_inventory_by_id(self, inventory_id: int) -> Inventory | None:
        """Metoda pobierająca pozycję inventory po ID.

        Args:
            inventory_id (int): ID pozycji inventory.

        Returns:
            Inventory | None: Pozycja inventory, jeśli istnieje, lub None.
        """
        return await self._repository.show_inventory_by_id(inventory_id)

    async def get_all_inventory(self) -> Iterable[Inventory]:
        """Metoda pobierająca wszystkie pozycje inventory.

        Returns:
            Iterable[Inventory]: Kolekcja wszystkich pozycji inventory.
        """
        return await self._repository.get_all_inventory()

    async def add_inventory(self, data: InventoryIn) -> Inventory | None:
        """Metoda dodająca nową pozycję inventory.

        Args:
            data (InventoryIn): Atrybuty nowej pozycji inventory.

        Returns:
            Inventory | None: Nowo utworzona pozycja inventory, lub None, jeśli operacja się nie powiodła.
        """
        
        return await self._repository.add_inventory(data)

    async def update_inventory(self, inventory_id: int, data: InventoryIn) -> Inventory | None:
        """Metoda aktualizująca istniejącą pozycję inventory.

        Args:
            inventory_id (int): ID pozycji inventory do zaktualizowania.
            data (InventoryIn): Zaktualizowane atrybuty pozycji inventory.

        Returns:
            Inventory | None: Zaktualizowana pozycja inventory lub None, jeśli operacja się nie powiodła.
        """
        return await self._repository.update_inventory(inventory_id, data)

    async def remove_inventory(self, inventory_id: int) -> bool:
        """Metoda usuwająca pozycję inventory.

        Args:
            inventory_id (int): ID pozycji inventory do usunięcia.

        Returns:
            bool: Powodzenie operacji usuwania.
        """
        return await self._repository.remove_inventory(inventory_id)
