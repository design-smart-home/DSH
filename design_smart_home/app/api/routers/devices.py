from fastapi import APIRouter, HTTPException
from app.services.device_api import DeviceAPI
from app.api.schemas.device import (
    ResponseGetDevice,
    RequestCreateDevice,
    ResponseCreateDevice,
    RequestUpdateDevice,
)
from app.core.authorization import get_current_user_from_token, get_user_id_from_token

import uuid

from httpx import Response


device_router = APIRouter()

base_url = "http://db_online:8001"
auth_url = "http://db_users:8002"
device_api = DeviceAPI(base_url)


@device_router.post("/", response_model=ResponseCreateDevice) # http://site.ru/devices/
def create_device(body: RequestCreateDevice):
    jwt_token = body.jwt_token
    user_id = get_user_id_from_token(jwt_token, auth_url)
    created_device_json = device_api.create_device(
        user_id=user_id,
        name=body.name,
        data_type=body.data_type,
        range_value=body.range_value,
        current_value=body.current_value,
    )

    if not created_device_json:
        raise HTTPException(status_code=404, detail=f"Failed created device.")
    # add raises

    return ResponseCreateDevice(
        device_id=created_device_json["device_id"],
        name=created_device_json["name"],
    )


@device_router.get("/{device_id}", response_model=ResponseGetDevice) # http://site.ru/devices/fmwoseig
def get_device(device_id: uuid.UUID):
    device_json = device_api.get_device(device_id)

    if not device_json:
        raise HTTPException(status_code=404, detail=f"Device with ID {device_id} not found.")
    # add any raises

    current_value = 0 if "current_value" not in device_json else device_json["current_value"]

    return ResponseGetDevice(
        device_id=device_json["device_id"],
        name=device_json["name"],
        data_type=device_json["data_type"],
        range_value=device_json["range_value"],
        current_value=current_value,
    )


@device_router.patch("/{device_id}", response_model=None)
def update_device(device_id: uuid.UUID, body: RequestUpdateDevice) -> Response:
    updated_device = device_api.update_device(device_id, body)

    if not updated_device:
        raise HTTPException(status_code=400, detail=f"Unknown error.")

    return Response(status_code=200, json={"message": "Successfully update device."})


@device_router.delete("/{device_id}", response_model=None)
def delete_device(device_id: uuid.UUID) -> Response:
    deleted_device = device_api.delete_device(device_id)

    if not deleted_device:
        raise HTTPException(status_code=400, detail="Unknown error.")

    return Response(status_code=200, json={"message": "Successfully deleted."})


@device_router.get("/all_devices/{jwt_token}")
def get_all_devices_by_user_id(jwt_token: str):
    user_id = get_user_id_from_token(jwt_token, auth_url)

    devices = device_api.get_all_devices_by_user_id(user_id)

    return devices
