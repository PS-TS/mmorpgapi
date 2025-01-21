"""Abstrakcyjne repozytorium user"""


from abc import ABC, abstractmethod
from typing import Any

from pydantic import UUID5

from src.core.domain.user import UserIn


class IUserRepository(ABC):
    """Abstrakcyjna klasa repozytorium user"""

    @abstractmethod
    async def register_user(self, user: UserIn) -> Any | None:
        """Metoda rejestrująca user

        Args:
            user (UserIn): Dane user

        Returns:
            Any | None: Nowy obiekt user
        """

    @abstractmethod
    async def get_by_uuid(self, uuid: UUID5) -> Any | None:
        """Metoda pobrania user przez uuid

        Args:
            uuid (UUID5): UUID user.

        Returns:
            Any | None: Obiekt user.
        """

    @abstractmethod
    async def get_by_email(self, email: str) -> Any | None:
        """Metoda pobrania user przez email.

        Args:
            email (str): Email user

        Returns:
            Any | None: Obiekt user.
        """