from abc import ABC, abstractmethod
from typing import Iterable

from src.core.domain.inventory import Inventory, InventoryIn


class IInventoryService(ABC):
    """Abstrakcyjna klasa reprezentująca protokół serwisu dla inventory."""

    @abstractmethod
    async def get_inventory_by_id(self, inventory_id: int) -> Inventory | None:
        """Abstrakcyjna metoda pobierania inventory po ID

        Args:
            inventory_id (int): ID pozycji inventory.

        Returns:
            Inventory | None: Pozycja inventory, jeśli istnieje, lub None w przeciwnym wypadku.
        """
    
    @abstractmethod
    async def get_all_inventory(self) -> Iterable[Inventory]:
        """Abstrakcyjna metoda pobierania wszystkich pozycji inventory

        Returns:
            Iterable[Inventory]: Kolekcja wszystkich pozycji inventory.
        """
    
    @abstractmethod
    async def add_inventory(self, data: InventoryIn) -> Inventory | None:
        """Abstrakcyjna metoda dodawania nowej pozycji inventory

        Args:
            data (InventoryIn): Atrybuty nowej pozycji inventory.

        Returns:
            Inventory | None: Nowo utworzona pozycja inventory, lub None w przypadku niepowodzenia operacji.
        """
    
    @abstractmethod
    async def update_inventory(self, inventory_id: int, data: InventoryIn) -> Inventory | None:
        """Abstrakcyjna metoda aktualizacji pozycji inventory

        Args:
            inventory_id (int): ID pozycji inventory do zaktualizowania.
            data (InventoryIn): Zaktualizowane atrybuty pozycji inventory.

        Returns:
            Inventory | None: Zaktualizowana pozycja inventory lub None, jeśli operacja się nie powiodła.
        """
    
    @abstractmethod
    async def remove_inventory(self, inventory_id: int) -> bool:
        """Abstrakcyjna metoda usuwania pozycji inventory

        Args:
            inventory_id (int): ID pozycji inventory do usunięcia.

        Returns:
            bool: Powodzenie operacji usuwania.
        """
