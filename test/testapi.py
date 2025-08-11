from unittest.mock import patch
from myproject.flightapi import fetch_flight_data

@patch("myproject.flightapi.requests.get")
def test_fetch_flight_data(mock_get):
    fake_response = {
        "flight_id": "F301",
        "origin": "Delhi",
        "destination": "Mumbai",
        "price": 5000,
        "available_seats": 30
    }

    mock_get.return_value.json.return_value = fake_response

    result = fetch_flight_data("F301")
    assert result["flight_id"] == "F301"
    assert result["price"] == 5000
    mock_get.assert_called_once_with("https://example.com/api/flights/F301")
