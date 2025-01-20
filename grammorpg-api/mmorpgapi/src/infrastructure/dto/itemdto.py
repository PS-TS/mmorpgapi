"""A module containing DTO models for item."""

from pydantic import BaseModel, ConfigDict  # type: ignore


class ItemDTO(BaseModel):
    """A model representing DTO for item data."""
    id: int
    name: str

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        arbitrary_types_allowed=True,
    )
