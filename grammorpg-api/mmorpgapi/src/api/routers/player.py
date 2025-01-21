"""Moduł zawierający endpointy dla playera."""

from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from src.container import Container
from src.core.domain.player import Player, PlayerIn
from src.infrastructure.services.iplayer import IPlayerService

router = APIRouter()


@router.post("/create", response_model=Player, status_code=201)
@inject
async def create_player(
    player: PlayerIn,
    service: IPlayerService = Depends(Provide[Container.player_service]),
) -> dict:
    """Dodanie nowego playera.

    Args:
        player (PlayerIn): Dane playera.
        service (IPlayerService): Serwis playerów.

    Raises:
        HTTPException: Jeśli player z tą nazwą już istnieje.

    Returns:
        dict: Utworzony player.
    """
    try:
        new_player = await service.add_player(player)
        return new_player.model_dump() if new_player else {}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/all", response_model=Iterable[Player], status_code=200)
@inject
async def get_all_players(
    service: IPlayerService = Depends(Provide[Container.player_service]),
) -> Iterable:
    """Endpoint pobierający wszystkich playerów.

    Args:
        service (IPlayerService, optional): Wstrzykiwana zależność serwisu.

    Returns:
        Iterable: Kolekcja playerów.
    """
    players = await service.get_all_players()
    return players


@router.get("/{player_id}", response_model=Player, status_code=200)
@inject
async def get_player_by_id(
    player_id: int,
    service: IPlayerService = Depends(Provide[Container.player_service]),
) -> dict:
    """Endpoint pobierający dane playera po ID.

    Args:
        player_id (int): ID playera.
        service (IPlayerService, optional): Wstrzykiwana zależność serwisu.

    Raises:
        HTTPException: 404 jeśli player nie istnieje.

    Returns:
        dict: Atrybuty playera.
    """
    if player := await service.get_player_by_id(player_id):
        return player.model_dump()

    raise HTTPException(status_code=404, detail="Player not found")


@router.put("/{player_id}", response_model=Player, status_code=201)
@inject
async def update_player(
    player_id: int,
    updated_player: PlayerIn,
    service: IPlayerService = Depends(Provide[Container.player_service]),
) -> dict:
    """Endpoint aktualizujący dane playera.

    Args:
        player_id (int): ID playera.
        updated_player (PlayerIn): Zaktualizowane dane playera.
        service (IPlayerService, optional): Wstrzykiwana zależność serwisu.

    Raises:
        HTTPException: 404 jeśli player nie istnieje.

    Returns:
        dict: Zaktualizowane dane playera.
    """
    if await service.get_player_by_id(player_id=player_id):
        new_updated_player = await service.update_player(
            player_id=player_id,
            data=updated_player,
        )
        return new_updated_player.model_dump() if new_updated_player else {}

    raise HTTPException(status_code=404, detail="Player not found")


@router.delete("/{player_id}", status_code=204)
@inject
async def delete_player(
    player_id: int,
    service: IPlayerService = Depends(Provide[Container.player_service]),
) -> None:
    """Endpoint usuwający playera.

    Args:
        player_id (int): ID playera.
        service (IPlayerService, optional): Wstrzykiwana zależność serwisu.

    Raises:
        HTTPException: 404 jeśli player nie istnieje.

    Returns:
        None: Puste, jeśli operacja zakończona sukcesem.
    """
    if await service.get_player_by_id(player_id=player_id):
        await service.delete_player(player_id)
        return

    raise HTTPException(status_code=404, detail="Player not found")
