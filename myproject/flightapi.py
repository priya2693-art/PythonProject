import requests

def fetch_flight_data(flight_id):
    url = f"https://example.com/api/flights/{flight_id}"
    response = requests.get(url)
    return response.json()
