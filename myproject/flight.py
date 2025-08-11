
class Flight:
    def __init__(self, flight_id, origin, destination, price, available_seats):
        self.flight_id = flight_id
        self.origin = origin
        self.destination = destination
        self.price = price
        self.available_seats = available_seats

    def is_available(self, seats):
        return self.available_seats >= seats

    def book_seats(self, seats):
        if not self.is_available(seats):
            raise ValueError("Not enough seats available")
        self.available_seats -= seats
        return True

    def cancel_seats(self, seats):
        self.available_seats += seats
        return True

    def get_price_for_seats(self, seats):
        return self.price * seats

    def get_flight_info(self):
        return {
            "flight_id": self.flight_id,
            "origin": self.origin,
            "destination": self.destination,
            "price": self.price,
            "available_seats": self.available_seats
        }
