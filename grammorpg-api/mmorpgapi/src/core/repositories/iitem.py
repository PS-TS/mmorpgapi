"""Abstrakcje repozytorium item"""

from abc import ABC, abstractmethod
from typing import Any, Iterable

from src.core.domain.item import ItemIn


class IItemRepository(ABC):
    """Abstrakcyjna klasa repozytoria item"""

    @abstractmethod
    async def get_item_by_id(self, item_id: int) -> Any | None:
        """Abstrakcyjna metoda pobierania pozycji item po id

        Args:
            item_id (int): id itemu.

        Returns:
            Any | None: Item jeśli istnieje.
        """

    @abstractmethod
    async def get_all_items(self) -> Iterable[Any]:
        """Abstrakcyjna metoda pobierania wszystkich item

        Returns:
            Iterable[Any]: Zwraca kolekcję wszystkich itemów
        """

    @abstractmethod
    async def get_item_by_name(self, name: str) -> Any | None:
        """Abstrakcyjna metoda pobierania pozycji item po name

        Args:
            name (str): Nazwa itemu name

        Returns:
            Any | None: Item jeśli istnieje
        """

    @abstractmethod
    async def add_item(self, data: ItemIn) -> Any | None:
        """Abstrakcyjna metoda dodawania pozycji item

        Args:
            data (ItemIn): Atrybuty itemu

        Returns:
            Any | None: Nowo utworzony item
        """

    @abstractmethod
    async def update_item(self, item_id: int, data: ItemIn) -> Any | None:
        """Abstrakcyjna metoda aktualizacji pozycji item

        Args:
            item_id (int): Id itemu
            data (ItemIn): Atrybuty itemu

        Returns:
            Any | None: Nadpisany item
        """

    @abstractmethod
    async def delete_item(self, item_id: int) -> bool:
        """Abstrakcyjna metoda usuwania pozycji item

        Args:
            item_id (int): ID itemu

        Returns:
            bool: Powodzenie operacji
        """
