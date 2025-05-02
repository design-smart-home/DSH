from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.schemas.device import (
    GetDeviceResponse,
    PostDeviceRequest,
    PostDeviceResponse,
)
from app.api.core.device import (
    delete_device_by_name,    get_device_by_id,
    post_device_, get_all_devices_by_user_id_
)

import uuid

from httpx import Response


device_router = APIRouter()


@device_router.get("/{device_id}/1.1")
def get_device(
    device_id: uuid.UUID, db: Session = Depends(get_db)
) -> GetDeviceResponse:
    device = get_device_by_id(device_id, session=db)

    if not device:
        raise HTTPException(
            status_code=404, detail=f"Device by name {device_id} not found"
        )

    return GetDeviceResponse(
        device_id=device.device_id,
        name=device.name,
        data_type=device.data_type,
        range_value=device.range_value,
        current_value=device.current_value,
    )


@device_router.post("/")
def post_device(
    body: PostDeviceRequest, db: Session = Depends(get_db)
) -> PostDeviceResponse:
    device = post_device_(body, session=db)

    if not device:
        raise HTTPException(status_code=400, detail="Unknown error")

    return PostDeviceResponse(
        device_id=device.device_id,
        name=device.name,
    )


@device_router.delete("/{device_id}", response_model=None)
def delete_device(
    device_id: uuid.UUID, db: Session = Depends(get_db)
) -> Response:
    device = delete_device_by_name(device_id, session=db)

    if not device:
        raise HTTPException(
            status_code=404, detail=f"Device with ID {device_id} not found"
        )

    return Response(status_code=200)


@device_router.get("/all_devices/{user_id}")
def get_all_devices_by_user_id(user_id: uuid.UUID, db: Session = Depends(get_db)):
    devices = get_all_devices_by_user_id_(user_id, db)

    return devices
