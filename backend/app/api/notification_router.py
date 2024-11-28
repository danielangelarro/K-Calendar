import uuid
import inject
from fastapi import APIRouter, Request, HTTPException
from app.api.decorators import require_authentication
from app.application.services.notification_service import INotificationService
from app.domain.models.schemma import NotificationResponse

router = APIRouter()


@router.get("/notifications", response_model=list[NotificationResponse])
@require_authentication
async def get_notifications(request: Request):
    notification_service: INotificationService = inject.instance(INotificationService)
    current_user = request.state.current_user
    notifications = await notification_service.get_notifications(current_user.id)
    return notifications


@router.post("/notifications/mark_as_read")
@require_authentication
async def mark_as_read(notification_ids: list[uuid.UUID], request: Request):
    notification_service: INotificationService = inject.instance(INotificationService)
    await notification_service.mark_as_read(notification_ids)
    return {"detail": "Notifications marked as read successfully"}
