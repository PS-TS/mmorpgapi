from typing import Optional, List
from pydantic import BaseModel, ConfigDict, UUID4

class MarketIn(BaseModel):
    item_id: int
    seller_id: UUID4
    price: float
    quantity: int


class Market(MarketIn):
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")
