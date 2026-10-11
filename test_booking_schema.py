import pytest
import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from schemas.booking_schema import BOOKING_SCHEMA

BASE_URL = "https://restful-booker.herokuapp.com"


def test_get_booking_schema():
    response_ids = requests.get(f"{BASE_URL}/booking")
    assert response_ids.status_code == 200
    booking_id = response_ids.json()[0]["bookingid"]

    response = requests.get(f"{BASE_URL}/booking/{booking_id}")
    assert response.status_code == 200

    validate(instance=response.json(), schema=BOOKING_SCHEMA)


def test_booking_schema_invalid_data_fails():
    """Negative Test: Verify that an invalid data contract triggers a ValidationError."""
    corrupt_payload = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": "one hundred",  # Schema expects number, got string
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2026-01-05"
        }
    }

    with pytest.raises(ValidationError):
        validate(instance=corrupt_payload, schema=BOOKING_SCHEMA)