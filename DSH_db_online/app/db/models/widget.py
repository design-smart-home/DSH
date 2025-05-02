from email.policy import default

from app.db.base import Base
from pyasn1.type.univ import Boolean
from sqlalchemy import UUID, String, ARRAY, Integer
from sqlalchemy.orm import Mapped, mapped_column
import uuid


class Widget(Base):
    __tablename__ = "widgets"

    widget_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), nullable=False
    )
    device_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True)
    )
    type_widget: Mapped[str] = mapped_column(String(10), nullable=False)
    current_value: Mapped[int] = mapped_column(Integer, default=0)
    name: Mapped[str] = mapped_column(String(20), nullable=False)

# check name column type_device
