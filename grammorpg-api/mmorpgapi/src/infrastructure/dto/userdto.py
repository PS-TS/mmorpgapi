
from pydantic import UUID4, BaseModel, ConfigDict


class UserDTO(BaseModel):
    """Model DTO dla user"""

    id: UUID4
    email: str

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )