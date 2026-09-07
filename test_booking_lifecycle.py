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