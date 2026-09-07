# RESTful-Booker Automated Test Suite

An automated API regression test suite built with **Python**, **Pytest**, and **Requests** targeting the [Restful-Booker](https://restful-booker.herokuapp.com) API.

## Features
- **Session-scoped Authentication**: Automatically acquires a bearer token via `/auth` in `conftest.py`.
- **Dynamic Test Fixtures**: Creates and passes clean `booking_id` entities per test run to prevent test pollution.
- **Data-Driven Testing**: Uses `@pytest.mark.parametrize` to run batch CRUD validations against diverse payloads.
- **Negative Testing Scenarios**:
  - `403 Forbidden` response validation for invalid/expired tokens.
  - `405 Method Not Allowed` response validation for operations against non-existent booking IDs.

## Test Execution

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yilmacareerist/api_practice.git](https://github.com/yilmacareerist/api_practice.git)
   cd api_practice