"""Moduł zawierający abstrakcje repozytorium player."""

from abc import ABC, abstractmethod
from typing import Any

from src.core.domain.player import PlayerIn


class IPlayerRepository(ABC):
    """Abstrakcyjna klasa repozytorium player"""

    @abstractmethod
    async def add_player(self, data: PlayerIn) -> Any | None:
        """Abstrakcyjna metoda dodawania playera

        Args:
            data (PlayerIn): Atrybuty playera

        Returns:
            Any | None: Nowo utworzony player lub None, jeśli operacja się nie powiodła
        """

    @abstractmethod
    async def update_player(self, player_id: int, data: PlayerIn) -> Any | None:
        """Abstrakcyjna metoda aktualizacji playera

        Args:
            player_id (int): ID playera do zaktualizowania
            data (PlayerIn): Zaktualizowane atrybuty playera

        Returns:
            Any | None: Zaktualizowany player lub None, jeśli operacja się nie powiodła
        """

    @abstractmethod
    async def remove_player(self, player_id: int) -> bool:
        """Abstrakcyjna metoda usuwania playera

        Args:
            player_id (int): ID playera do usunięcia

        Returns:
            bool: Powodzenie operacji usuwania
        """

    @abstractmethod
    async def get_player_by_id(self, player_id: int) -> Any | None:
        """Abstrakcyjna metoda pobierania playera po ID

        Args:
            player_id (int): ID playera do pobrania

        Returns:
            Any | None: Player, jeśli istnieje, lub None w przeciwnym wypadku
        """

    @abstractmethod
    async def get_player_by_name(self, name: str) -> Any | None:
        """Abstrakcyjna metoda pobierania playera po nazwie

        Args:
            name (str): Nazwa playera do pobrania

        Returns:
            Any | None: Player, jeśli istnieje, lub None w przeciwnym wypadku
        """