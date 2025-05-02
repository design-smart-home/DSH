from app.api.schemas.device import PostDeviceRequest
from app.db.models.device import Device
from app.db.repository.device import DeviceRepository
from sqlalchemy.orm import Session

from typing import Type
import uuid


def get_device_by_id(device_id: uuid.UUID, session: Session) -> Type[Device] | None:
    device_repo = DeviceRepository(session)

    device = device_repo.get_device(device_id=device_id)

    if device:
        return device


def post_device_(data: PostDeviceRequest, session: Session) -> Device | None:
    device_repo = DeviceRepository(session)

    device = device_repo.post_device(
        user_id=data.user_id,
        name=data.name,
        data_type=data.data_type,
        range_value=data.range_value,
        current_value=data.current_value,
    )

    if device:
        return device


def delete_device_by_name(
    device_id: uuid.UUID, session: Session
) -> Type[Device] | None:
    device_repo = DeviceRepository(session)

    device = device_repo.delete_device(device_id=device_id)

    if device:
        return device


def get_all_devices_by_user_id_(user_id: uuid.UUID, session: Session) -> list[Type[Device]] | None:
    device_repo = DeviceRepository(session)

    devices = device_repo.get_all_devices_by_user_id(user_id)

    return devices
