"""Moduł zawierający implementację repozytorium player."""

from typing import Any, Iterable

from asyncpg import Record  # type: ignore

from src.core.domain.player import Player, PlayerIn
from src.core.repositories.iplayer import IPlayerRepository
from src.db import player_table, database


class PlayerRepository(IPlayerRepository):
    """Klasa implementująca repozytorium player."""

    async def get_player_by_id(self, player_id: int) -> Any | None:
        """Metoda pobierająca playera z magazynu danych po ID.

        Args:
            player_id (int): ID playera.

        Returns:
            Any | None: Dane playera, jeśli istnieje.
        """
        player = await self._get_by_id(player_id)
        return Player(**dict(player)) if player else None

    async def get_player_by_name(self, name: str) -> Any | None:
        """Metoda pobierająca playera z magazynu danych po nazwie.

        Args:
            name (str): Nazwa playera.

        Returns:
            Any | None: Dane playera, jeśli istnieje.
        """
        query = (
            player_table.select()
            .where(player_table.c.name == name)
            .order_by(player_table.c.name.asc())
        )
        player = await database.fetch_one(query)
        return Player(**dict(player)) if player else None

    async def add_player(self, data: PlayerIn) -> Any | None:
        """Metoda dodająca nowego playera do magazynu danych.

        Args:
            data (PlayerIn): Atrybuty playera.

        Returns:
            Any | None: Nowo utworzony player, jeśli operacja się powiodła.
        """
        query = player_table.insert().values(**data.model_dump())
        new_player_id = await database.execute(query)
        new_player = await self._get_by_id(new_player_id)
        return Player(**dict(new_player)) if new_player else None

    async def update_player(self, player_id: int, data: PlayerIn) -> Any | None:
        """Metoda aktualizująca dane playera w magazynie danych.

        Args:
            player_id (int): ID playera.
            data (PlayerIn): Zaktualizowane atrybuty playera.

        Returns:
            Any | None: Zaktualizowany player, jeśli operacja się powiodła.
        """
        if await self._get_by_id(player_id):
            query = (
                player_table.update()
                .where(player_table.c.id == player_id)
                .values(**data.model_dump())
            )
            await database.execute(query)
            updated_player = await self._get_by_id(player_id)
            return Player(**dict(updated_player)) if updated_player else None
        return None

    async def remove_player(self, player_id: int) -> bool:
        """Metoda usuwająca playera z magazynu danych.

        Args:
            player_id (int): ID playera do usunięcia.

        Returns:
            bool: Powodzenie operacji usuwania.
        """
        if await self._get_by_id(player_id):
            query = player_table.delete().where(player_table.c.id == player_id)
            await database.execute(query)
            return True
        return False

    async def _get_by_id(self, player_id: int) -> Record | None:
        """Prywatna metoda pobierająca playera z bazy danych na podstawie ID.

        Args:
            player_id (int): ID playera.

        Returns:
            Record | None: Rekord playera, jeśli istnieje.
        """
        query = (
            player_table.select()
            .where(player_table.c.id == player_id)
            .order_by(player_table.c.name.asc())
        )
        return await database.fetch_one(query)
