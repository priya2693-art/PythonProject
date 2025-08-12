from myproject.hotel import Hotel


class HotelBooking:
    def __init__(self,booking_id,hotel:Hotel,customer_name,rooms,nights):
        if not isinstance(hotel,Hotel):
            raise TypeError("Invalid hotel object provided")

        if rooms<=0 or nights<=0:
            raise ValueError("Rooms and nights must be positive ")

        self.booking_id= booking_id
        self.hotel =hotel
        self.customer_name= customer_name
        self.rooms= rooms
        self.nights= nights
        self.is_cancelled= False
        self.total_price= self.hotel.get_price_for_rooms(rooms,nights)

        self.hotel.book_rooms(rooms)

    def cancel_booking(self):
        if not self.is_cancelled:
            self.hotel.cancel_rooms(self.rooms)
            self.is_cancelled = True
            return True
        return False

    def get_booking_info(self):
        return {
            "booking_id": self.booking_id,
            "hotel": self.hotel,
            "customer_name": self.customer_name,
            "rooms": self.rooms,
            "nights": self.nights,
            "total_price": self.total_price,
            "is_cancelled": self.is_cancelled
        }