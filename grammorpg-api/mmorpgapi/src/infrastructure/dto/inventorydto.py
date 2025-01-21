from pydantic import BaseModel, ConfigDict 


class InventoryDTO(BaseModel):
    """Model DTO dla inventory"""
    id: int
    money: int
    itemlist: str

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        arbitrary_types_allowed=True,
    )
