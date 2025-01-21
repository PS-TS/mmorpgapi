"""A module containing item endpoints."""

from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from src.container import Container
from src.core.domain.item import Item, ItemIn
from src.infrastructure.services.iitem import IItemService

router = APIRouter()


@router.post("/create", response_model=Item, status_code=201)
@inject
async def create_item(
    item: ItemIn,
    service: IItemService = Depends(Provide[Container.item_service]),
) -> dict:
    """Add new item
    Args:
        item (ItemIn): Item data.
        service (IItemService): Item service

    Raises:
        HTTPException: If id is already used

    Returns:
        dict: Created item.
    """
    try:
        new_item = await service.add_item(item)
        return new_item.model_dump() if new_item else {}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/all", response_model=Iterable[Item], status_code=200)
@inject
async def get_all_items(
    service: IItemService = Depends(Provide[Container.item_service]),
) -> Iterable:
    """An endpoint for getting all items.

    Args:
        service (IItemService, optional): The injected service dependency.

    Returns:
        Iterable: The item attributes collection.
    """

    items = await service.get_all_items()

    return items


@router.get("/{item_id}", response_model=Item, status_code=200)
@inject
async def get_item_by_id(
    item_id: int,
    service: IItemService = Depends(Provide[Container.item_service]),
) -> dict:
    """An endpoint for getting item details by id.

    Args:
        item_id (int): The id of the item.
        service (IItemService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if item does not exist.

    Returns:
        dict: The requested item attributes.
    """

    if item := await service.get_item_by_id(item_id):
        return item.model_dump()

    raise HTTPException(status_code=404, detail="Item not found")


@router.put("/{item_id}", response_model=Item, status_code=201)
@inject
async def update_item(
    item_id: int,
    updated_item: ItemIn,
    service: IItemService = Depends(Provide[Container.item_service]),
) -> dict:
    """An endpoint for updating item data.

    Args:
        item_id (int): The id of the item.
        updated_item (ItemIn): The updated item details.
        service (IItemService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if item does not exist.

    Returns:
        dict: The updated item details.
    """

    if await service.get_item_by_id(item_id=item_id):
        new_updated_item = await service.update_item(
            item_id=item_id,
            data=updated_item,
        )
        return new_updated_item.model_dump() if new_updated_item else {}

    raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/{item_id}", status_code=204)
@inject
async def delete_item(
    item_id: int,
    service: IItemService = Depends(Provide[Container.item_service]),
) -> None:
    """An endpoint for deleting items.

    Args:
        item_id (int): The id of the item.
        service (IItemService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if item does not exist.

    Returns:
        None: Empty if operation finished.
    """

    if await service.get_item_by_id(item_id=item_id):
        await service.delete_item(item_id)
        return

    raise HTTPException(status_code=404, detail="Item not found")
