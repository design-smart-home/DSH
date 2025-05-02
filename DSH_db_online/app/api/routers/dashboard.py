from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.schemas.dashboard import (
    GetDashboardResponse,
    PostDashboardRequest,
    PostDashboardResponse,
    GetAllDashboardsResponse,
)
from app.api.core.dashboard import (
    get_dashboard_by_id, post_dashboard_, get_dashboards_by_user_id
)

import uuid


dashboard_router = APIRouter()


@dashboard_router.get("/{dashboard_id}")
def get_dashboard(
    dashboard_id: uuid.UUID, db: Session = Depends(get_db)
) -> GetDashboardResponse:
    dashboard = get_dashboard_by_id(dashboard_id, session=db)

    if not dashboard:
        raise HTTPException(
            status_code=404, detail=f"Dashboard by name {dashboard_id} not found"
        )

    return GetDashboardResponse(
        dashboard_id=dashboard.dashboard_id,
        user_id=dashboard.user_id,
        devices_ids=dashboard.devices_ids,
        name=dashboard.name
    )


@dashboard_router.post("/")
def post_dashboard(
    body: PostDashboardRequest, db: Session = Depends(get_db)
) -> PostDashboardResponse:
    dashboard = post_dashboard_(body, session=db)

    if not dashboard:
        raise HTTPException(status_code=400, detail="Unknown error")

    return PostDashboardResponse(
        dashboard_id=dashboard.dashboard_id,
        devices_ids=dashboard.devices_ids
    )


@dashboard_router.get("/all_dashboards/{user_id}")
def get_all_dashboards(user_id: uuid.UUID, db: Session = Depends(get_db)):
    dashboards = get_dashboards_by_user_id(user_id, db)

    return GetAllDashboardsResponse(
        dashboards=[GetDashboardResponse(
            dashboard_id=dashboard.dashboard_id,
            user_id=dashboard.user_id,
            devices_ids=dashboard.devices_ids,
            name=dashboard.name
        ) for dashboard in dashboards]
    )


# @widget_router.delete("/{widget_id}", response_model=None)
# def delete_widget(
#     widget_id: uuid.UUID, db: Session = Depends(get_db)
# ) -> Response:
#     widget = delete_widget_by_name(widget_id, session=db)
#
#     if not widget:
#         raise HTTPException(
#             status_code=404, detail=f"Widget with ID {widget_id} not found"
#         )
#
#     return Response(status_code=200)
#
#
# @widget_router.patch("/{widget_id}")
# def update_widget(
#     widget_id: uuid.UUID,
#     device_id: uuid.UUID | None = None,
#     type_widget: str | None = None,
#     current_value: int | None = None,
#     name: str | None = None,
#     db: Session = Depends(get_db)
# ):
#     widget = update_widget_(
#         db,
#         widget_id,
#         device_id,
#         type_widget,
#         current_value,
#         name
#     )
#
#     if widget:
#         return {"status_code": 200, "message": "OK"}
