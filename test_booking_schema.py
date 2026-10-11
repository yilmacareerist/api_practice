import requests
from jsonschema import validate
from schemas.booking_schema import BOOKING_SCHEMA

BASE_URL = "https://restful-booker.herokuapp.com"

def test_get_booking_schema():
    response_ids = requests.get(f"{BASE_URL}/booking")
    assert response_ids.status_code == 200
    booking_id = response_ids.json()[0]["bookingid"]

    response = requests.get(f"{BASE_URL}/booking/{booking_id}")
    assert response.status_code == 200

    validate(instance=response.json(), schema=BOOKING_SCHEMA)