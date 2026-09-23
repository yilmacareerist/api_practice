import pytest
import requests
from faker import Faker

fake = Faker()
BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="session")
def auth_token():
    """Generates an authentication token valid for the whole test session."""
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(f"{BASE_URL}/auth", json=payload)
    assert response.status_code == 200, "Authentication failed"
    token = response.json().get("token")
    assert token is not None, "Token missing from auth response"
    return token


@pytest.fixture
def dynamic_booking_payload():
    """Generates a dynamic, randomized booking payload for testing."""
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=50, max=500),
        "depositpaid": fake.boolean(),
        "bookingdates": {
            "checkin": fake.date_this_year().strftime("%Y-%m-%d"),
            "checkout": fake.future_date().strftime("%Y-%m-%d")
        },
        "additionalneeds": fake.random_element(
            elements=["Breakfast", "Late Checkout", "Airport Shuttle", "Crib"]
        )
    }


@pytest.fixture
def booking_id(dynamic_booking_payload):
    """Creates a booking using dynamic data and returns its bookingid."""
    response = requests.post(f"{BASE_URL}/booking", json=dynamic_booking_payload)
    assert response.status_code == 200, f"Booking creation failed: {response.text}"
    data = response.json()
    assert "bookingid" in data, f"Booking creation missing bookingid: {data}"
    return data["bookingid"]


# Alias in case any tests use created_booking_id
@pytest.fixture
def created_booking_id(booking_id):
    return booking_id