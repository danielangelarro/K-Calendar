import uuid
import inject

from fastapi import APIRouter
from fastapi import Request
from fastapi import HTTPException

from app.api.decorators import require_authentication
from app.domain.models.schemma import GroupCreate, GroupResponse
from app.application.services.group_service import IGroupService

router = APIRouter()


@router.post("/groups/", response_model=GroupResponse)
@require_authentication
async def create_group(group_create: GroupCreate, request: Request):
    group_service: IGroupService = inject.instance(IGroupService)
    return await group_service.create_group(group_create)


@router.get("/groups/{group_id}", response_model=GroupResponse)
@require_authentication
async def get_group(group_id: uuid.UUID, request: Request):
    group_service: IGroupService = inject.instance(IGroupService)
    group = await group_service.get_group(group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group


@router.put("/groups/{group_id}", response_model=GroupResponse)
@require_authentication
async def update_group(group_id: uuid.UUID, group_update: GroupCreate, request: Request):
    group_service: IGroupService = inject.instance(IGroupService)
    updated_group = await group_service.update_group(group_id, group_update)
    if not updated_group:
        raise HTTPException(status_code=404, detail="Group not found")
    return updated_group


@router.delete("/groups/{group_id}")
@require_authentication
async def delete_group(group_id: uuid.UUID, request: Request):
    group_service: IGroupService = inject.instance(IGroupService)
    await group_service.delete_group(group_id)
    return {"detail": "Group deleted successfully"}
