from typing import Optional, List
from pydantic import BaseModel, ConfigDict, UUID4

class PlayerIn(BaseModel):
    login: str
    password: str


class Player(PlayerIn):
    id: UUID4

    model_config = ConfigDict(from_attributes=True, extra="ignore")
