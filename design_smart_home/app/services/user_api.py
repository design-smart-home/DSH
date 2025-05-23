import httpx
import requests
from uuid import UUID
import logging
logging.basicConfig(level=logging.DEBUG)

from app.api.schemas.user import RequestCreateUser, RequestUpdateUser


class UserAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_user(self, user_id: UUID):
        url = f"{self.base_url}/users/{user_id}"
        response = httpx.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get user with ID {user_id}. Status code: {response.status_code}")

    def get_user_by_email(self, email: str):
        url = f"{self.base_url}/users/by_email/{email}/"
        # http://127.0.0.1:8002/users/by_email/string
        # http://127.0.0.1:8002/users/by_email/string
        response = requests.get(url)
        # http: // 127.0.0.1: 8002 / users / by_email / wef
        print(url)
        try:
            return response.json()
        except Exception:
            return response

    def create_user(self, data: RequestCreateUser):
        url = f"{self.base_url}/users"
        response = requests.post(url, json=data.model_dump())
        try:
            return response.json()
        except Exception as e:
            raise Exception(f"Failed to create user. Status code: {response.status_code} {e}")

    def update_device(self, device_id: UUID, data: RequestUpdateUser):
        url = f"{self.base_url}/users/{device_id}/1.1/"
        response = httpx.put(url, json=data.model_dump())
        if response.status_code in [200, 204]:
            return response.json() if response.status_code == 200 else None
        else:
            raise Exception(f"Failed to update user with ID {device_id}. Status code: {response.status_code}")

    def delete_user(self, user_id):
        url = f"{self.base_url}/users/{user_id}"
        response = httpx.delete(url)
        if response.status_code in [200, 204]:
            return response.json()
        else:
            raise Exception(f"Failed to delete user with ID {user_id}. Status code: {response.status_code}")