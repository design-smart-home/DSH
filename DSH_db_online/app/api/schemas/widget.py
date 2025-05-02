from pydantic import BaseModel
import uuid


class GetWidgetResponse(BaseModel):
    widget_id: uuid.UUID
    user_id: uuid.UUID
    device_id: uuid.UUID | None
    type_widget: str
    current_value: int
    name: str


class PostWidgetRequest(BaseModel):
    user_id: uuid.UUID | str
    device_id: uuid.UUID | str | None
    type_widget: str
    current_value: int
    name: str



class PostWidgetResponse(BaseModel):
    widget_id: uuid.UUID
    device_id: uuid.UUID
    name: str
    type_widget: str
