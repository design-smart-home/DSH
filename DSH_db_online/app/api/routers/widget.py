from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.schemas.widget import (
    GetWidgetResponse,
    PostWidgetRequest,
    PostWidgetResponse,
)
from app.api.core.widget import (
    delete_widget_by_name, get_widget_by_id,
    post_widget_, update_widget_, get_all_widgets_on_dashboard_
)

import uuid

from httpx import Response


widget_router = APIRouter()


@widget_router.get("/{widget_id}")
def get_widget(
    widget_id: uuid.UUID, db: Session = Depends(get_db)
) -> GetWidgetResponse:
    widget = get_widget_by_id(widget_id, session=db)

    if not widget:
        raise HTTPException(
            status_code=404, detail=f"Widget by name {widget_id} not found"
        )

    return GetWidgetResponse(
        widget_id=widget.widget_id,
        user_id=widget.user_id,
        device_id=widget.device_id,
        type_widget=widget.type_widget,
        current_value=widget.current_value,
        name=widget.name
    )


@widget_router.post("/")
def post_widget(
    body: PostWidgetRequest, db: Session = Depends(get_db)
) -> PostWidgetResponse:
    widget = post_widget_(body, session=db)

    if not widget:
        raise HTTPException(status_code=400, detail="Unknown error")

    return PostWidgetResponse(
        widget_id=widget.widget_id,
        device_id=widget.device_id,
        name=widget.name,
        type_widget=widget.type_widget
    )


@widget_router.delete("/{widget_id}", response_model=None)
def delete_widget(
    widget_id: uuid.UUID, db: Session = Depends(get_db)
) -> Response:
    widget = delete_widget_by_name(widget_id, session=db)

    if not widget:
        raise HTTPException(
            status_code=404, detail=f"Widget with ID {widget_id} not found"
        )

    return Response(status_code=200)


@widget_router.patch("/{widget_id}")
def update_widget(
    widget_id: uuid.UUID,
    device_id: uuid.UUID | None = None,
    type_widget: str | None = None,
    current_value: int | None = None,
    name: str | None = None,
    db: Session = Depends(get_db)
):
    widget = update_widget_(
        db,
        widget_id,
        device_id,
        type_widget,
        current_value,
        name
    )

    if widget:
        return {"status_code": 200, "message": "OK"}


@widget_router.get("/widgets_on_dashboard/{dashboard_id}")
def get_all_widgets_on_dashboard(dashboard_id: uuid.UUID, db: Session = Depends(get_db)):
    widgets_on_dashboard = get_all_widgets_on_dashboard_(dashboard_id, db)

    return widgets_on_dashboard
