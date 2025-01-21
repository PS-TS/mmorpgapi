"""Moduł zawierający logikę biznesową itemu."""

from pydantic import BaseModel, ConfigDict


class ItemIn(BaseModel):
    """Wejściowy model itemu"""
    name: str


class Item(ItemIn):
    """Klasowy model itemu"""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")
