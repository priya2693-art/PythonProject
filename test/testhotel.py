import pytest
from myproject.hotel import Hotel


def test_hotel_initialization():
    hotel = Hotel("H101", "Taj Palace", "Delhi", 5000, 10)
    assert hotel.hotel_id == "H101"
    assert hotel.name == "Taj Palace"  # Fix: correct expected value
    assert hotel.location == "Delhi"
    assert hotel.price_per_night == 5000
    assert hotel.available_room == 10


def test_is_available_true():
    hotel= Hotel("H102","Sea View","GOA",3000,5)
    assert hotel.is_available(3) is True


def test_is_available_false():
    hotel = Hotel("H103", "Hill Top", "Manali", 2500, 2)
    assert hotel.is_available(5) is False


def test_book_rooms_success():
    hotel = Hotel("H104", "Sunrise Hotel", "Pune", 2000, 4)
    result = hotel.book_rooms(2)
    assert result is True
    assert hotel.available_room == 2


def test_book_rooms_failure():
    hotel = Hotel("H105", "Royal Stay", "Jaipur", 4000, 1)
    with pytest.raises(ValueError) as excinfo:
        hotel.book_rooms(3)
    assert "Not enough rooms available" in str(excinfo.value)


def test_cancel_rooms():
    hotel = Hotel("H106", "Grand Inn", "Bangalore", 3500, 5)
    hotel.book_rooms(2)
    hotel.cancel_rooms(2)
    assert hotel.available_room == 5


def test_get_price_for_rooms():
    hotel = Hotel("H107", "Lakeside", "Udaipur", 4500, 8)
    total_price = hotel.get_price_for_rooms(2, 3)  # 2 rooms × 3 nights
    assert total_price == 27000


def test_get_hotel_info():
    hotel = Hotel("H108", "Comfort Stay", "Mumbai", 3800, 6)
    info = hotel.get_hotel_info()
    assert info["hotel_id"] == "H108"
    assert info["name"] == "Comfort Stay"
    assert info["location"] == "Mumbai"
    assert info["price_per_night"] == 3800
    assert info["available_room"] == 6


def test_book_all_available_rooms():
    hotel = Hotel("H109", "Budget Inn", "Kolkata", 1500, 3)
    hotel.book_rooms(3)
    assert hotel.available_room == 0
    with pytest.raises(ValueError):
        hotel.book_rooms(1)


def test_multiple_bookings_and_cancellations():
    hotel = Hotel("H110", "Elite Lodge", "Chennai", 3200, 6)
    hotel.book_rooms(2)
    assert hotel.available_room == 4
    hotel.book_rooms(1)
    assert hotel.available_room == 3
    hotel.cancel_rooms(1)
    assert hotel.available_room == 4