from typing import Optional, List
from pydantic import BaseModel, ConfigDict, UUID4

class ItemIn(BaseModel):
    name: str
    description: Optional[str]
    rarity: str


class Item(ItemIn):
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")
