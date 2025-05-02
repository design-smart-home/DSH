from sqlalchemy.orm import Session

from app.db.models.dashboard import Dashboard
from typing import Type, List
import uuid


class DashboardRepository:
    def __init__(self, db: Session):
        self._db = db

    def get_dashboard(self, dashboard_id: uuid.UUID) -> Type[Dashboard] | None:
        dashboard = self._db.query(Dashboard).filter(Dashboard.dashboard_id == dashboard_id).first()

        if dashboard:
            return dashboard

    def post_dashboard(
        self,
        user_id: uuid.UUID | str | None,
        devices_ids: list[uuid.UUID],
        name: str,
    ) -> Dashboard:
        dashboard = Dashboard(
            user_id=user_id,
            devices_ids=devices_ids,
            name=name,
        )

        self._db.add(dashboard)
        self._db.commit()
        self._db.flush()

        return dashboard

    def delete_dashboard(self, dashboard_id: uuid.UUID) -> Type[Dashboard] | None:
        dashboard = self._db.query(Dashboard).filter(Dashboard.dashboard_id == dashboard_id).first()

        if dashboard:
            self._db.delete(dashboard)
            self._db.commit()
            self._db.flush()

            return dashboard

    def get_dashboards_by_user_id(self, user_id) -> list[Type[Dashboard]] | list:
        dashboards = self._db.query(Dashboard).filter(Dashboard.user_id == user_id).all()

        return [] if not dashboards else dashboards

    # def update_dashboard(
    #         self,
    #         widget_id: uuid.UUID,
    #         device_id: uuid.UUID | None = None,
    #         type_widget: str | None = None,
    #         current_value: int | None = None,
    #         name: str | None = None,
    # ) -> None:
    #     widget = self._db.query(Widget).filter(Widget.widget_id == widget_id).first()
    #     if not widget:
    #         raise Exception(f"Widget with id {widget_id} not found")
    #
    #     if device_id:
    #         widget.device_id = device_id
    #     if type_widget:
    #         widget.type_widget = type_widget
    #     if current_value:
    #         widget.current_value = current_value
    #     if name:
    #         widget.name = name
    #
    #     self._db.commit()
    #     self._db.flush()
