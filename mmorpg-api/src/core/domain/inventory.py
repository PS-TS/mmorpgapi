from typing import Optional, List
from pydantic import BaseModel, ConfigDict, UUID4

class InventoryIn(BaseModel):
    character_id: int
    item_id: int
    quantity: int


class Inventory(InventoryIn):
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")
