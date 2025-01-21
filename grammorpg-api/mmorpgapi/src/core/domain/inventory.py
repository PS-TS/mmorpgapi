"""Moduł zawierający logikę biznesową inventory."""

from pydantic import BaseModel, ConfigDict


class InventoryIn(BaseModel):
    """Wejściowy model inventory"""
    money: int
    itemlist: str


class Inventory(InventoryIn):
    """Klasowy model inventory"""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")

