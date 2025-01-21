"""Moduł zawierający logikę biznesową playera."""

from pydantic import BaseModel, ConfigDict


class PlayerIn(BaseModel):
    """Wejściowy model playera"""
    name: str
    strength: int
    hp: int
    maxhp: int
    connectedinventory: int


class Player(PlayerIn):
    """Klasowy model playera"""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")
