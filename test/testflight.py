import pytest
from myproject.flight import Flight


def test_flight_initialization():
    flight = Flight("F101", "Delhi", "Mumbai", 5000, 50)
    assert flight.flight_id == "F101"
    assert flight.origin == "Delhi"
    assert flight.destination == "Mumbai"
    assert flight.price == 5000
    assert flight.available_seats == 50


def test_flight_booking():
    flight = Flight("F102", "Delhi", "Goa", 4000, 10)
    result = flight.book_seats(3)
    assert result is True
    assert flight.available_seats == 7


def test_flight_overbooking():
    flight = Flight("F103", "Mumbai", "Pune", 2000, 2)
    with pytest.raises(ValueError):
        flight.book_seats(3)


def test_flight_cancel_seats():
    flight = Flight("F104", "Chennai", "Kolkata", 3500, 5)
    flight.book_seats(2)
    flight.cancel_seats(2)
    assert flight.available_seats == 5


def test_flight_book_all_available_seats():
    flight = Flight("F105", "Delhi", "Chandigarh", 3000, 3)
    flight.book_seats(3)
    assert flight.available_seats == 0
    with pytest.raises(ValueError):
        flight.book_seats(1)  # no seats left


def test_flight_multiple_bookings_and_cancellations():
    flight = Flight("F106", "Indore", "Hyderabad", 2800, 6)
    flight.book_seats(2)
    assert flight.available_seats == 4
    flight.book_seats(1)
    assert flight.available_seats == 3
    flight.cancel_seats(1)
    assert flight.available_seats == 4


def test_flight_get_price_for_seats():
    flight = Flight("F107", "Delhi", "Bhopal", 3500, 10)
    assert flight.get_price_for_seats(3) == 10500


def test_flight_is_available_true():
    flight = Flight("F108", "Goa", "Delhi", 4500, 10)
    assert flight.is_available(5) is True


def test_flight_is_available_false():
    flight = Flight("F109", "Goa", "Delhi", 4500, 2)
    assert flight.is_available(5) is False


def test_flight_get_flight_info():
    flight = Flight("F110", "Kolkata", "Ahmedabad", 5000, 15)
    info = flight.get_flight_info()
    assert info["flight_id"] == "F110"
    assert info["origin"] == "Kolkata"
    assert info["destination"] == "Ahmedabad"
    assert info["price"] == 5000
    assert info["available_seats"] == 15
