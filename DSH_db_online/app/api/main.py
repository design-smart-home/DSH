from fastapi import APIRouter

from app.api.routers.device import device_router
from app.api.routers.widget import widget_router
from app.api.routers.dashboard import dashboard_router

main_router = APIRouter()

main_router.include_router(device_router, prefix="/devices", tags=["devices"])
main_router.include_router(widget_router, prefix="/widgets", tags=["widgets"])
main_router.include_router(dashboard_router, prefix="/dashboards", tags=["dashboards"])
