from datetime import datetime


class Flight:
    def __init__(self, flight_id: str, origin: str, destination: str,
                 departure_time: datetime, arrival_time: datetime,
                 price: float, available_seats: int):
        if price < 0 or available_seats < 0:
            raise ValueError("Price and available seats must be non-negative.")

        self.flight_id = flight_id
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price
        self.available_seats = available_seats

    def book_seat(self, num_seats: int = 1) -> bool:
        if num_seats <= 0:
            raise ValueError("Number of seats must be positive.")
        if self.available_seats >= num_seats:
            self.available_seats -= num_seats
            return True
        return False