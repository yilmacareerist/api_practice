import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# 1. Validate Status Code
assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

# 2. Parse JSON Data
data = response.json()

# 3. Validate Payload Fields
assert data["id"] == 1, f"Expected id 1 but got {data['id']}"
assert data["userId"] == 1, f"Expected userId 1 but got {data['userId']}"
assert len(data["title"]) > 0, "Title should not be empty"

print("✅ All API assertions passed successfully!")
