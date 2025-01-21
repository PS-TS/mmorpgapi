"""Moduł zawierający logikę biznesową usera."""


from pydantic import BaseModel, ConfigDict, UUID1


class UserIn(BaseModel):
    """Wejściowy model usera"""
    email: str
    password: str


class User(UserIn):
    """Klasowy model usera"""
    id: UUID1

    model_config = ConfigDict(from_attributes=True, extra="ignore")