import requests

# 1. Define the endpoint and payload
url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "Automated Test Post",
    "body": "This post was created via automated Python script.",
    "userId": 1
}

# 2. Send the POST request
response = requests.post(url, json=payload)

# 3. Validate Creation Status (201 Created)
assert response.status_code == 201, f"Expected 201 Created but got {response.status_code}"

# 4. Validate Response Contains Generated ID
data = response.json()
assert data["id"] == 101, f"Expected created resource id 101, got {data['id']}"
assert data["title"] == payload["title"], "Returned title does not match payload"

print("✅ POST request assertions passed successfully!")
print("Server Response:", data)
