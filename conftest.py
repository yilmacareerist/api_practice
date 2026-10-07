import pytest
import requests
from faker import Faker

fake = Faker()

@pytest.fixture(scope="session")
def auth_token():
    url = "https://restful-booker.herokuapp.com/auth"
    payload = {"username": "admin", "password": "password123"}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200, f"Auth failed: {response.text}"
    token = response.json().get("token")
    assert token, "Token not found in response"
    return token

@pytest.fixture
def dynamic_booking_payload():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=50, max=500),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-10"
        },
        "additionalneeds": "Breakfast"
    }

@pytest.fixture
def booking_id(dynamic_booking_payload):
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.post(url, json=dynamic_booking_payload, headers=headers)
    assert response.status_code == 200, f"Booking creation failed: {response.text}"
    data = response.json()
    assert "bookingid" in data, f"Booking creation missing bookingid: {data}"
    return data["bookingid"]

@pytest.fixture
def created_booking_id(booking_id):
    return booking_id

@pytest.fixture(scope="session")
def base_url():
    return "https://restful-booker.herokuapp.com"



@pytest.fixture(scope="session")
def auth_token(base_url):
    url = f"{base_url}/auth"
    payload = {
        "username": "admin",
        "password": "password123"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200
    return response.json()["token"]


@pytest.fixture
def auth_headers(auth_token):
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={auth_token}"
    }
