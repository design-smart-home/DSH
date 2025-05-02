from sqlalchemy.orm import Session

from app.db.models.device import Device
from typing import Type, List
import uuid


class DeviceRepository:
    def __init__(self, db: Session):
        self._db = db

    def get_device(self, device_id: uuid.UUID) -> Type[Device] | None:
        device = self._db.query(Device).filter(Device.device_id == device_id).first()

        if device:
            return device

    def get_all_devices_by_user_id(self, user_id: uuid.UUID) -> list[Type[Device]] | None:
        devices = self._db.query(Device).filter(Device.user_id == user_id).all()

        return devices

    def post_device(
        self,
        user_id: uuid.UUID,
        name: str,
        data_type: str,
        range_value: list[int, int] | list[float, float],
        current_value: int,
    ) -> Device:
        device = Device(
            user_id=user_id,
            name=name,
            data_type=data_type,
            range_value=range_value,
            current_value=current_value,
        )

        self._db.add(device)
        self._db.commit()
        self._db.flush()

        return device

    def delete_device(self, device_id: uuid.UUID) -> Type[Device] | None:
        device = self._db.query(Device).filter(Device.device_id == device_id).first()

        if device:
            self._db.delete(device)
            self._db.commit()
            self._db.flush()

            return device
