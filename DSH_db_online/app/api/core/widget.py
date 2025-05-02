from app.api.schemas.widget import PostWidgetRequest
from app.db.models.widget import Widget
from app.db.repository.widget import WidgetRepository
from sqlalchemy.orm import Session

from typing import Type
import uuid


def get_widget_by_id(widget_id: uuid.UUID, session: Session) -> Type[Widget] | None:
    widget_repo = WidgetRepository(session)

    widget = widget_repo.get_widget(widget_id=widget_id)

    if widget:
        return widget


def post_widget_(data: PostWidgetRequest, session: Session) -> Widget | None:
    widget_repo = WidgetRepository(session)
    data

    if data.device_id:
        widget = widget_repo.post_widget(
            user_id=data.user_id,
            device_id=data.device_id,
            type_widget=data.type_widget,
            current_value=data.current_value,
            name=data.name,
        )
    else:
        widget = widget_repo.post_widget(
            user_id=data.user_id,
            type_widget=data.type_widget,
            current_value=data.current_value,
            name=data.name,
        )

    if widget:
        return widget


def delete_widget_by_name(
    widget_id: uuid.UUID, session: Session
) -> Type[Widget] | None:
    widget_repo = WidgetRepository(session)

    widget = widget_repo.delete_widget(widget_id=widget_id)

    if widget:
        return widget


def update_widget_(
        session: Session,
        widget_id: uuid.UUID,
        device_id: uuid.UUID | None = None,
        type_widget: str | None = None,
        current_value: int | None = None,
        name: str | None = None,
):
    widget_repo = WidgetRepository(session)

    updated_widget = widget_repo.update_widget(
        widget_id=widget_id,
        device_id=device_id,
        type_widget=type_widget,
        current_value=current_value,
        name=name,
    )

    return updated_widget


def get_all_widgets_on_dashboard_(dashboard_id: uuid.UUID, session: Session):
    widget_repo = WidgetRepository(session)

    widgets_on_dashboard = widget_repo.get_all_widgets_on_dashboard(dashboard_id)

    return widgets_on_dashboard