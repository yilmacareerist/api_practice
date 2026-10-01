import pytest
import requests

BOOKING_TEST_CASES = [
    (
        "Standard Booking",
        {
            "firstname": "Kenenisa",
            "lastname": "Bekele",
            "totalprice": 250,
            "depositpaid": True,
            "bookingdates": {"checkin": "2026-10-01", "checkout": "2026-10-10"},
            "additionalneeds": "Water",
        },
        200,
    ),
    (
        "Zero Total Price",
        {
            "firstname": "Derartu",
            "lastname": "Tulu",
            "totalprice": 0,
            "depositpaid": False,
            "bookingdates": {"checkin": "2026-12-01", "checkout": "2026-12-05"},
            "additionalneeds": "Extra Towels",
        },
        200,
    ),
    (
        "Special Characters in Name",
        {
            "firstname": "Tirunesh-Dibaba",
            "lastname": "O'Connor",
            "totalprice": 1200,
            "depositpaid": True,
            "bookingdates": {"checkin": "2027-01-10", "checkout": "2027-01-20"},
            "additionalneeds": "Late Checkout",
        },
        200,
    ),
]


@pytest.mark.parametrize("test_name, payload, expected_status", BOOKING_TEST_CASES)
def test_create_booking_data_driven(base_url, auth_headers, test_name, payload, expected_status):
    """Data-driven test verifying booking creation across varying inputs and boundary data."""
    res = requests.post(f"{base_url}/booking", json=payload)
    assert res.status_code == expected_status, f"Failed on scenario: {test_name}"

    data = res.json()
    assert "bookingid" in data
    assert data["booking"]["firstname"] == payload["firstname"]
    assert data["booking"]["totalprice"] == payload["totalprice"]

    # Teardown: clean up created booking
    booking_id = data["bookingid"]
    del_res = requests.delete(f"{base_url}/booking/{booking_id}", headers=auth_headers)
    assert del_res.status_code == 201