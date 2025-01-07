from typing import Optional, List
from pydantic import BaseModel, ConfigDict, UUID4

class CharacterIn(BaseModel):
    name: str
    level: int
    player_id: UUID4


class Character(CharacterIn):
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")
