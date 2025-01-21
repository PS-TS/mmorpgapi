from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from src.container import Container
from src.core.domain.inventory import Inventory, InventoryIn
from src.infrastructure.services.iinventory import IInventoryService

router = APIRouter()


@router.post("/create", response_model=Inventory, status_code=201)
@inject
async def create_inventory(
    inventory: InventoryIn,
    service: IInventoryService = Depends(Provide[Container.inventory_service]),
) -> dict:
    """Add new inventory
    Args:
        inventory (InventoryIn): Inventory data.
        service (IInventoryService): Inventory service

    Raises:
        HTTPException: If operation fails

    Returns:
        dict: Created inventory.
    """
    try:
        new_inventory = await service.add_inventory(inventory)
        return new_inventory.model_dump() if new_inventory else {}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/all", response_model=Iterable[Inventory], status_code=200)
@inject
async def get_all_inventory(
    service: IInventoryService = Depends(Provide[Container.inventory_service]),
) -> Iterable:
    """An endpoint for getting all inventories.

    Args:
        service (IInventoryService, optional): The injected service dependency.

    Returns:
        Iterable: The inventory attributes collection.
    """

    inventory = await service.get_all_inventory()

    return inventory


@router.get("/{inventory_id}", response_model=Inventory, status_code=200)
@inject
async def get_inventory_by_id(
    inventory_id: int,
    service: IInventoryService = Depends(Provide[Container.inventory_service]),
) -> dict:
    """An endpoint for getting inventory details by id.

    Args:
        inventory_id (int): The id of the inventory.
        service (IInventoryService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if inventory does not exist.

    Returns:
        dict: The requested inventory attributes.
    """

    if inventory := await service.get_inventory_by_id(inventory_id):
        return inventory.model_dump()

    raise HTTPException(status_code=404, detail="Inventory not found")


@router.put("/{inventory_id}", response_model=Inventory, status_code=201)
@inject
async def update_inventory(
    inventory_id: int,
    updated_inventory: InventoryIn,
    service: IInventoryService = Depends(Provide[Container.inventory_service]),
) -> dict:
    """An endpoint for updating inventory data.

    Args:
        inventory_id (int): The id of the inventory.
        updated_inventory (InventoryIn): The updated inventory details.
        service (IInventoryService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if inventory does not exist.

    Returns:
        dict: The updated inventory details.
    """

    if await service.get_inventory_by_id(inventory_id=inventory_id):
        new_updated_inventory = await service.update_inventory(
            inventory_id=inventory_id,
            data=updated_inventory,
        )
        return new_updated_inventory.model_dump() if new_updated_inventory else {}

    raise HTTPException(status_code=404, detail="Inventory not found")


@router.delete("/{inventory_id}", status_code=204)
@inject
async def delete_inventory(
    inventory_id: int,
    service: IInventoryService = Depends(Provide[Container.inventory_service]),
) -> None:
    """An endpoint for deleting inventory.

    Args:
        inventory_id (int): The id of the inventory.
        service (IInventoryService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if inventory does not exist.

    Returns:
        None: Empty if operation finished.
    """

    if await service.get_inventory_by_id(inventory_id=inventory_id):
        await service.remove_inventory(inventory_id)
        return

    raise HTTPException(status_code=404, detail="Inventory not found")
