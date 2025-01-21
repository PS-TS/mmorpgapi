"""Moduł zawierający implementację usług player."""

from typing import Iterable

from src.core.domain.player import Player, PlayerIn
from src.core.repositories.iplayer import IPlayerRepository
from src.infrastructure.services.iplayer import IPlayerService


class PlayerService(IPlayerService):
    """Klasa implementująca usługę player."""

    _repository: IPlayerRepository

    def __init__(self, repository: IPlayerRepository) -> None:
        """Inicjalizator klasy `PlayerService`.

        Args:
            repository (IPlayerRepository): Referencja do repozytorium player.
        """

        self._repository = repository

    async def get_player_by_id(self, player_id: int) -> Player | None:
        """Metoda pobierająca playera z repozytorium po ID.

        Args:
            player_id (int): ID playera.

        Returns:
            Player | None: Dane playera, jeśli istnieje.
        """
        return await self._repository.get_player_by_id(player_id)

    async def get_player_by_name(self, name: str) -> Player | None:
        """Metoda pobierająca playera z repozytorium po nazwie.

        Args:
            name (str): Nazwa playera.

        Returns:
            Player | None: Dane playera, jeśli istnieje.
        """
        return await self._repository.get_player_by_name(name)

    async def add_player(self, data: PlayerIn) -> Player | None:
        """Metoda dodająca nowego playera do repozytorium.

        Args:
            data (PlayerIn): Atrybuty playera.

        Returns:
            Player | None: Nowo utworzony player, jeśli operacja się powiodła.
        """
        existing_player = await self._repository.get_player_by_name(data.name)
        if existing_player:
            raise ValueError(f"Player with name '{data.name}' already exists.")

        return await self._repository.add_player(data)

    async def update_player(self, player_id: int, data: PlayerIn) -> Player | None:
        """Metoda aktualizująca dane playera w repozytorium.

        Args:
            player_id (int): ID playera.
            data (PlayerIn): Zaktualizowane atrybuty playera.

        Returns:
            Player | None: Zaktualizowany player, jeśli operacja się powiodła.
        """
        existing_player = await self._repository.get_player_by_id(player_id)
        if not existing_player:
            raise ValueError(f"Player with ID {player_id} does not exist.")

        return await self._repository.update_player(player_id, data)

    async def delete_player(self, player_id: int) -> bool:
        """Metoda usuwająca playera z repozytorium.

        Args:
            player_id (int): ID playera.

        Returns:
            bool: Powodzenie operacji usuwania.
        """
        existing_player = await self._repository.get_player_by_id(player_id)
        if not existing_player:
            raise ValueError(f"Player with ID {player_id} does not exist.")

        return await self._repository.remove_player(player_id)
