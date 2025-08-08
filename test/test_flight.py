import pytest
from datetime import datetime, timedelta
from myproject.flight import Flight
# === Flight Tests ===

def test_flight_initialization():
    dep = datetime.now()
    arr = dep + timedelta(hours=2)
    flight = Flight("F001", "DEL", "MUM", dep, arr, 3000, 100)
    assert flight.flight_id == "F001"
    assert flight.origin == "DEL"
    assert flight.destination == "MUM"
    assert flight.price == 3000
    assert flight.available_seats == 100

def test_flight_booking_success():
    flight = Flight("F002", "DEL", "GOA", datetime.now(), datetime.now(), 2500, 3)
    result = flight.book_seat(2)
    assert result is True
    assert flight.available_seats == 1

def test_flight_booking_failure():
    flight = Flight("F003", "DEL", "GOA", datetime.now(), datetime.now(), 2500, 1)
    result = flight.book_seat(2)
    assert result is False
    assert flight.available_seats == 1

def test_flight_invalid_inputs():
    with pytest.raises(ValueError):
        Flight("F004", "DEL", "NYC", datetime.now(), datetime.now(), -1000, 10)

    with pytest.raises(ValueError):
        Flight("F005", "DEL", "NYC", datetime.now(), datetime.now(), 1000, -5)

    flight = Flight("F006", "DEL", "MUM", datetime.now(), datetime.now(), 2000, 10)
    with pytest.raises(ValueError):
        flight.book_seat(0)