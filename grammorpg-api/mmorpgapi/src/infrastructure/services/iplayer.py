"""Moduł zawierający abstrakcje usług player."""

from abc import ABC, abstractmethod
from typing import Iterable

from src.core.domain.player import Player, PlayerIn


class IPlayerService(ABC):
    """Abstrakcyjna klasa reprezentująca protokół usługi player."""

    @abstractmethod
    async def get_player_by_id(self, player_id: int) -> Player | None:
        """Abstrakcyjna metoda pobierająca playera z repozytorium.

        Args:
            player_id (int): ID playera.

        Returns:
            Player | None: Dane playera, jeśli istnieje.
        """

    @abstractmethod
    async def get_player_by_name(self, name: str) -> Player | None:
        """Abstrakcyjna metoda pobierająca playera z repozytorium po nazwie.

        Args:
            name (str): Nazwa playera.

        Returns:
            Player | None: Dane playera, jeśli istnieje.
        """

    @abstractmethod
    async def add_player(self, data: PlayerIn) -> Player | None:
        """Abstrakcyjna metoda dodająca nowego playera do repozytorium.

        Args:
            data (PlayerIn): Atrybuty playera.

        Returns:
            Player | None: Nowo utworzony player.
        """

    @abstractmethod
    async def update_player(self, player_id: int, data: PlayerIn) -> Player | None:
        """Abstrakcyjna metoda aktualizująca dane playera w repozytorium.

        Args:
            player_id (int): ID playera.
            data (PlayerIn): Atrybuty playera.

        Returns:
            Player | None: Zaktualizowany player.
        """

    @abstractmethod
    async def delete_player(self, player_id: int) -> bool:
        """Abstrakcyjna metoda usuwająca playera z repozytorium.

        Args:
            player_id (int): ID playera.

        Returns:
            bool: Powodzenie operacji usuwania.
        """
