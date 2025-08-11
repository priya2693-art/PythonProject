# test/test_booking.py

import pytest
from myproject.flight import Flight
from myproject.booking import Booking


def test_booking_success():
    flight = Flight("F201", "Delhi", "Bangalore", 6000, 20)
    booking = Booking("Amit", flight, 4)
    assert booking.passenger_name == "Amit"
    assert booking.status == "CONFIRMED"
    assert booking.amount == 24000
    assert flight.available_seats == 16


def test_booking_insufficient_seats():
    flight = Flight("F202", "Delhi", "Goa", 4500, 2)
    with pytest.raises(ValueError):
        Booking("Neha", flight, 5)


def test_booking_cancellation():
    flight = Flight("F203", "Pune", "Delhi", 4000, 5)
    booking = Booking("Ravi", flight, 2)
    booking.cancel()
    assert booking.status == "CANCELLED"
    assert flight.available_seats == 5


def test_booking_double_cancel():
    flight = Flight("F204", "Delhi", "Lucknow", 3000, 3)
    booking = Booking("Priya", flight, 1)
    booking.cancel()
    with pytest.raises(ValueError):
        booking.cancel()


def test_booking_partial_vs_full_capacity():
    flight = Flight("F205", "Indore", "Chennai", 2000, 5)
    booking1 = Booking("Ankit", flight, 2)
    booking2 = Booking("Sneha", flight, 3)
    assert flight.available_seats == 0
    with pytest.raises(ValueError):
        Booking("Riya", flight, 1)


def test_booking_get_info():
    flight = Flight("F206", "Kolkata", "Jaipur", 3500, 4)
    booking = Booking("Tina", flight, 2)
    info = booking.get_booking_info()
    assert info["passenger_name"] == "Tina"
    assert info["flight"]["origin"] == "Kolkata"
    assert info["amount"] == 7000
    assert info["status"] == "CONFIRMED"


def test_booking_is_active_status():
    flight = Flight("F207", "Surat", "Nagpur", 1800, 5)
    booking = Booking("Raj", flight, 2)
    assert booking.is_active() is True
    booking.cancel()
    assert booking.is_active() is False


def test_multiple_bookings_affect_seat_count():
    flight = Flight("F208", "Amritsar", "Leh", 4200, 10)
    Booking("Pooja", flight, 3)
    Booking("Kunal", flight, 2)
    assert flight.available_seats == 5


def test_booking_zero_seats_should_fail():
    flight = Flight("F209", "Mumbai", "Patna", 5000, 10)
    with pytest.raises(ValueError):
        Booking("Dummy", flight, 0)  # Edge case: booking 0 seats


def test_booking_negative_seats_should_fail():
    flight = Flight("F210", "Agra", "Delhi", 5000, 10)
    with pytest.raises(ValueError):
        Booking("Dummy", flight, -2)
