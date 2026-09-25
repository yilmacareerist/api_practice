from jsonschema import validate
import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com"

def test_update_booking_put(auth_token, booking_id):
    url = f"{BASE_URL}/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={auth_token}"
    }
    payload = {
        "firstname": "Abebe",
        "lastname": "Bikila",
        "totalprice": 180,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-11-01",
            "checkout": "2026-11-05"
        },
        "additionalneeds": "Energy Bar"
    }
    response = requests.put(url, json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["firstname"] == "Abebe"
    assert data["totalprice"] == 180


def test_delete_booking(auth_token, booking_id):
    url = f"{BASE_URL}/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={auth_token}"
    }
    response = requests.delete(url, headers=headers)
    assert response.status_code == 201


@pytest.mark.parametrize("first,last,price", [
    ("Abebe", "Bikila", 120),
    ("Haile", "Gebrselassie", 250),
    ("Derartu", "Tulu", 310)
])
def test_update_booking_parametrized(auth_token, booking_id, first, last, price):
    url = f"{BASE_URL}/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={auth_token}"
    }
    payload = {
        "firstname": first,
        "lastname": last,
        "totalprice": price,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-12-01",
            "checkout": "2026-12-05"
        },
        "additionalneeds": "Supplements"
    }
    response = requests.put(url, json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["firstname"] == first
    assert data["totalprice"] == price


def test_update_booking_with_invalid_token(booking_id):
    """Ensure updating without a valid token is rejected with 403 Forbidden."""
    url = f"{BASE_URL}/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": "token=invalid_token_12345"
    }
    payload = {
        "firstname": "Hacker",
        "lastname": "Attempt",
        "totalprice": 999,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-10-01",
            "checkout": "2026-10-05"
        },
        "additionalneeds": "Free Stay"
    }
    response = requests.put(url, json=payload, headers=headers)
    assert response.status_code == 403


def test_delete_non_existent_booking(auth_token):
    """Ensure deleting an invalid booking ID returns 405 Method Not Allowed."""
    invalid_id = 99999999
    url = f"{BASE_URL}/booking/{invalid_id}"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={auth_token}"
    }
    response = requests.delete(url, headers=headers)
    assert response.status_code == 405

    from jsonschema import validate

# Schema definition for RESTful-Booker booking object
BOOKING_SCHEMA = {
    "type": "object",
    "properties": {
        "firstname": {"type": "string"},
        "lastname": {"type": "string"},
        "totalprice": {"type": "integer"},
        "depositpaid": {"type": "boolean"},
        "bookingdates": {
            "type": "object",
            "properties": {
                "checkin": {"type": "string"},
                "checkout": {"type": "string"}
            },
            "required": ["checkin", "checkout"]
        },
        "additionalneeds": {"type": "string"}
    },
    "required": ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates"]
}

def test_get_booking_schema_validation(booking_id):
    """Fetch booking and validate complete JSON schema structure and types."""
    url = f"{BASE_URL}/booking/{booking_id}"
    headers = {"Accept": "application/json"}
    
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    
    data = response.json()
    # validate() raises ValidationError if response breaks the contract
    validate(instance=data, schema=BOOKING_SCHEMA)