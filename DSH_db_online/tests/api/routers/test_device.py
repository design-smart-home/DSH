import uuid

import pytest

from app.db.models.device import Device


@pytest.fixture
def params():
    return {
        "device_id": str(uuid.uuid4()),
        "name": "TestName",
        "data_type": "input",
        "range_value": [0],
        "current_value": 0,
    }


def test_create_device_in_db(db, create_device_in_db, params):
    create_device_in_db(
        device_id=params["device_id"],
        name=params["name"],
        data_type=params["data_type"],
        range_value=params["range_value"],
        current_value=params["current_value"],
        session=db,
    )

    device = db.query(Device).filter(Device.device_id == params["device_id"]).first()

    assert device is not None


def test_post_device(db, client, params):
    response = client.post(f"devices/", json=params)
    assert response.status_code == 200
    assert response.json()["name"] == params["name"]

    device = db.query(Device).filter(Device.device_id == response.json()["device_id"]).first()

    assert device is not None


def test_get_device(db, client, create_device_in_db, params):
    create_device_in_db(**params, session=db)

    response = client.get(f"devices/{params['device_id']}/1.1")

    assert response.status_code == 200
    assert response.json() == {
        "device_id": params["device_id"],
        "name": params["name"],
        "data_type": params["data_type"],
        "range_value": params["range_value"],
        "current_value": params["current_value"],
    }


def test_delete_device(db, client, create_device_in_db, params):
    create_device_in_db(**params, session=db)

    response = client.delete(f"devices/{params['device_id']}")

    assert response.status_code == 200

    device = db.query(Device).filter(Device.device_id == params["device_id"]).first()

    assert device is None
