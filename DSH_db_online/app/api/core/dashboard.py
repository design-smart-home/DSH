from app.api.schemas.dashboard import PostDashboardRequest
from app.db.models.dashboard import Dashboard
from app.db.repository.dashboard import DashboardRepository
from sqlalchemy.orm import Session

from typing import Type
import uuid


def get_dashboard_by_id(dashboard_id: uuid.UUID, session: Session) -> Type[Dashboard] | None:
    dashboard_repo = DashboardRepository(session)

    dashboard = dashboard_repo.get_dashboard(dashboard_id=dashboard_id)

    if dashboard:
        return dashboard


def post_dashboard_(data: PostDashboardRequest, session: Session) -> Dashboard | None:
    dashboard_repo = DashboardRepository(session)

    dashboard = dashboard_repo.post_dashboard(
        user_id=data.user_id,
        devices_ids=data.devices_ids,
        name=data.name
    )

    if dashboard:
        return dashboard


def get_dashboards_by_user_id(user_id: uuid.UUID, session: Session) -> list[Dashboard]:
    dashboard_repo = DashboardRepository(session)

    dashboards = dashboard_repo.get_dashboards_by_user_id(user_id)

    return dashboards


# def delete_widget_by_name(
#     widget_id: uuid.UUID, session: Session
# ) -> Type[Widget] | None:
#     widget_repo = WidgetRepository(session)
#
#     widget = widget_repo.delete_widget(widget_id=widget_id)
#
#     if widget:
#         return widget


# def update_widget_(
#         session: Session,
#         widget_id: uuid.UUID,
#         device_id: uuid.UUID | None = None,
#         type_widget: str | None = None,
#         current_value: int | None = None,
#         name: str | None = None,
# ):
#     widget_repo = WidgetRepository(session)
#
#     updated_widget = widget_repo.update_widget(
#         widget_id=widget_id,
#         device_id=device_id,
#         type_widget=type_widget,
#         current_value=current_value,
#         name=name,
#     )
#
#     return updated_widget
