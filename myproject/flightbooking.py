
from datetime import datetime

class Booking:
    def __init__(self, passenger_name, flight, seats):
        if not flight.is_available(seats):
            raise ValueError("Flight does not have enough seats")

        self.passenger_name = passenger_name
        self.flight = flight
        self.seats = seats
        self.amount = flight.get_price_for_seats(seats)
        self.status = "CONFIRMED"
        self.date = datetime.now()

        flight.book_seats(seats)

    def cancel(self):
        if self.status == "CANCELLED":
            raise ValueError("Booking already cancelled")

        self.flight.cancel_seats(self.seats)
        self.status = "CANCELLED"
        return True

    def is_active(self):
        return self.status == "CONFIRMED"

    def get_booking_info(self):
        return {
            "passenger_name": self.passenger_name,
            "flight": self.flight.get_flight_info(),
            "seats": self.seats,
            "amount": self.amount,
            "status": self.status,
            "date": self.date.strftime("%Y-%m-%d %H:%M")
        }
