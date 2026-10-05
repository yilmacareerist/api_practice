import requests

# 1. Request a resource ID that does not exist
url = "https://jsonplaceholder.typicode.com/posts/9999"
response = requests.get(url)

# 2. Assert that the server returns 404 Not Found
assert response.status_code == 404, f"Expected 404 but got {response.status_code}"

# 3. Assert that response body is empty (or an empty dictionary)
data = response.json()
assert data == {}, f"Expected empty payload for non-existent resource, got {data}"

print("✅ Negative test passed: 404 Not Found verified correctly!")
