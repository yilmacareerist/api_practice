import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com"

@pytest.fixture(scope="session")
def auth_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(f"{BASE_URL}/auth", json=payload)
    assert response.status_code == 200
    token = response.json().get("token")
    assert token is not None, "Failed to retrieve auth token"
    return token

@pytest.fixture
def booking_id():
    payload = {
        "firstname": "Yilma",
        "lastname": "Tester",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-10-01",
            "checkout": "2026-10-05"
        },
        "additionalneeds": "Late Checkout"
    }
    response = requests.post(f"{BASE_URL}/booking", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "bookingid" in data, f"Booking creation failed: {data}"
    return data["bookingid"]