import requests
import json

# URL of your Flask app (change if deployed)
url = 'http://127.0.0.1:8081/cluster'

# Sample data for latitudes and longitudes
sample_latitudes = [37.7749, 34.0522, 40.7128, 41.8781]
sample_longitudes = [-122.4194, -118.2437, -74.0060, -87.6298]

# Prepare the data payload
payload = {'latitudes': sample_latitudes, 'longitudes': sample_longitudes}

# Send POST request
response = requests.post(url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    print("Location Clustering Results:")
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Error: Unable to get a response. Status code: {response.status_code}")