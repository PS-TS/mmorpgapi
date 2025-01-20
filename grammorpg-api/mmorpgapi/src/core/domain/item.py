"""Module containing location-related domain models."""

from pydantic import BaseModel, ConfigDict


class ItemIn(BaseModel):
    """Model representing item's DTO attributes."""
    name: str


class Item(ItemIn):
    """Model representing item's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")
