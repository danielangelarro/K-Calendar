from datetime import datetime
import uuid
import inject
from app.application.repositories.agenda_repository import IAgendaRepository
from app.application.services.agenda_service import IAgendaService
from app.domain.models.schemma import UserAgendaResponse


class AgendaService(IAgendaService):
    repo_instance: IAgendaRepository = inject.attr(IAgendaRepository)

    async def get_user_agenda(self, user_id: uuid.UUID, start_date: datetime, end_date: datetime) -> UserAgendaResponse:
        return await self.repo_instance.get_user_agenda(user_id, start_date, end_date)

    async def get_group_agenda(self, group_id: uuid.UUID, start_date: datetime, end_date: datetime) -> list[UserAgendaResponse]:
        return await self.repo_instance.get_group_agenda(group_id, start_date, end_date)