from pydantic import BaseModel
import uuid


class GetDashboardResponse(BaseModel):
    dashboard_id: uuid.UUID
    user_id: uuid.UUID
    devices_ids: list[uuid.UUID]
    name: str


class PostDashboardRequest(BaseModel):
    user_id: str
    devices_ids: list[uuid.UUID]
    name: str


class PostDashboardResponse(BaseModel):
    dashboard_id: uuid.UUID
    devices_ids: list[uuid.UUID]


class GetAllDashboardsResponse(BaseModel):
    dashboards: list[GetDashboardResponse]
