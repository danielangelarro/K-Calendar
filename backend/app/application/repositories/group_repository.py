import uuid

from abc import ABC, abstractmethod
from app.domain.models.schemma import GroupCreate
from app.domain.models.schemma import GroupResponse


class IGroupRepository(ABC):
    @abstractmethod
    async def create(self, group_create: GroupCreate) -> GroupResponse:
        pass

    @abstractmethod
    async def get_by_id(self, group_id: uuid.UUID) -> GroupResponse:
        pass

    @abstractmethod
    async def update(self, group_id: uuid.UUID, group_data: GroupCreate) -> GroupResponse:
        pass

    @abstractmethod
    async def delete(self, group_id: uuid.UUID):
        pass