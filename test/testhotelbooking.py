import pytest
from myproject.hotel import Hotel
from myproject.hotelbooking import HotelBooking


def test_successful_booking():
    hotel = Hotel("H01","TAJ","Delhi",5000,10)
    booking= HotelBooking("B01",hotel,"nidhi",2,3)

    assert booking.total_price== 2*3*5000
    assert hotel.available_room==8
    assert booking.is_cancelled is False


def test_successful_cancellation():
    hotel = Hotel("H02", "Oberoi", "Mumbai", 4000, 5)
    booking = HotelBooking("B02", hotel, "Priya", 1, 2)

    result = booking.cancel_booking()
    assert result is True
    assert hotel.available_room == 5
    assert booking.is_cancelled is True

def test_booking_fails_when_rooms_not_available():
    hotel= Hotel("H04","lEELA","GOA",6000,1)
    HotelBooking("B04",hotel,"nisha",1,1)

    with pytest.raises(ValueError):
        HotelBooking("B05",hotel,"Aman",1,1)


def test_booking_with_zero_rooms():
    hotel= Hotel("H05","TAJ","Delhi",40000,2)

    with pytest.raises(ValueError):
        HotelBooking("B05",hotel,"nisha",0,1)


def test_booking_with_negative_rooms():
    hotel= Hotel("H06","the park","Pune",40000,2)

    with pytest.raises(ValueError):
        HotelBooking("B06",hotel,"vidhi",-2,2)

def test_booking_with_zero_nights():
    hotel =Hotel("H06","MANU MAHARANI","Mumbai",10000,3)

    with pytest.raises(ValueError):
        HotelBooking("B06", hotel, "vidhi", 2, 0)



