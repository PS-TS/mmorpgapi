"""Abstrakcyjne repozytorium inventory."""

from abc import ABC, abstractmethod
from typing import Any

from src.core.domain.inventory import InventoryIn


class IInventoryRepository(ABC):
    """Abstrakcyjna klasa repozytorium inventory"""

    @abstractmethod
    async def add_inventory(self, data: InventoryIn) -> Any | None:
        """Abstrakcyjna metoda dodawania pozycji inventory

        Args:
            data (InventoryIn): Atrybuty pozycji inventory

        Returns:
            Any | None: Nowo utworzona pozycja inventory lub None, jeśli operacja się nie powiodła
        """

    @abstractmethod
    async def update_inventory(self, inventory_id: int, data: InventoryIn) -> Any | None:
        """Abstrakcyjna metoda aktualizacji pozycji inventory

        Args:
            inventory_id (int): ID pozycji inventory do zaktualizowania
            data (InventoryIn): Zaktualizowane atrybuty pozycji inventory

        Returns:
            Any | None: Zaktualizowana pozycja inventory lub None, jeśli operacja się nie powiodła
        """

    @abstractmethod
    async def remove_inventory(self, inventory_id: int) -> bool:
        """Abstrakcyjna metoda usuwania pozycji inventory

        Args:
            inventory_id (int): ID pozycji inventory do usunięcia

        Returns:
            bool: Powodzenie operacji usuwania
        """

    @abstractmethod
    async def show_inventory_by_id(self, inventory_id: int) -> Any | None:
        """Abstrakcyjna metoda pobierania pozycji inventory po ID

        Args:
            inventory_id (int): ID pozycji inventory do pobrania

        Returns:
            Any | None: Pozycja inventory, jeśli istnieje, lub None w przeciwnym wypadku
        """

