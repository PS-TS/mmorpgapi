
class IPlayerRepository(ABC):
    """An abstract repository class for players."""

    @abstractmethod
    async def add_player(self, player: PlayerIn) -> Any | None:
        pass

    @abstractmethod
    async def delete_player(self, player_id: UUID4) -> bool:
        pass

    @abstractmethod
    async def update_player(self, player_id: UUID4, data: PlayerIn) -> Any | None:
        pass

    @abstractmethod
    async def get_by_id(self, player_id: UUID4) -> Any | None:
        pass
