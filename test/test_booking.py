
from myproject.booking import FlightBookingService
from unittest.mock import MagicMock

def test_successful_booking():
    mock_gateway = MagicMock()
    mock_gateway.charge.return_value = True

    service = FlightBookingService(mock_gateway)
    result = service.book_flight(5000)

    assert result == "Booking Confirmed"
    mock_gateway.charge.assert_called_once_with(5000)

def test_failed_booking():
    mock_gateway = MagicMock()
    mock_gateway.charge.return_value = False

    service = FlightBookingService(mock_gateway)
    result = service.book_flight(5000)

    assert result == "Payment Failed"
    mock_gateway.charge.assert_called_once()
