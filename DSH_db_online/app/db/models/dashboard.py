from app.db.base import Base
from sqlalchemy import UUID, String, ARRAY, Integer
from sqlalchemy.orm import Mapped, mapped_column
import uuid


class Dashboard(Base):
    __tablename__ = "dashboards"

    dashboard_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    devices_ids: Mapped[list[uuid.UUID]] = mapped_column(ARRAY(UUID)) # its widgets_ids!
    name: Mapped[str] = mapped_column(String(20), nullable=False)
