from app.db.base import Base
from sqlalchemy import UUID, String, ARRAY, Integer
from sqlalchemy.orm import Mapped, mapped_column
import uuid


class Device(Base):
    __tablename__ = "devices"

    device_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    data_type: Mapped[str] = mapped_column(String(10), nullable=False)
    range_value: Mapped[list[int, int] | list[float, float]] = mapped_column(ARRAY(Integer), nullable=False)
    current_value: Mapped[int] = mapped_column(Integer(), nullable=False)

# check name column type_device
