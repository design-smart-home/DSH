from pydantic import BaseModel
import uuid


class GetDeviceResponse(BaseModel):
    device_id: uuid.UUID
    name: str
    data_type: str
    range_value: list[int, int] | list[float, float]
    current_value: int


class PostDeviceRequest(BaseModel):
    name: str
    data_type: str
    range_value: list[int, int] | list[float, float]
    current_value: int


class PostDeviceResponse(BaseModel):
    device_id: uuid.UUID
    name: str
