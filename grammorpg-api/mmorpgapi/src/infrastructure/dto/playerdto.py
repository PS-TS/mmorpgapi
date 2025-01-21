from pydantic import BaseModel, ConfigDict  # type: ignore


class PlayerDTO(BaseModel):
    """Model DTO dla player"""
    id: int
    name: str
    strength: int
    hp: int
    maxhp: int
    connectedinventory: int

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        arbitrary_types_allowed=True,
    )
