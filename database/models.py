from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Flight(Base):
    __tablename__ = 'flights'

    def get_flight_info(self):
        return {
            "id": self.id,
            "flight_id": self.flight_id,
            "origin": self.origin,
            "destination": self.destination,
            "price": self.price,
            "available_seats": self.available_seats
        }

    id = Column(Integer, primary_key=True)
    flight_id = Column(String, unique=True)
    origin = Column(String)
    destination = Column(String)
    price = Column(Float)
    available_seats = Column(Integer)

    bookings = relationship("Booking", back_populates="flight")

    def is_available(self, seats):
        return self.available_seats >= seats

    def book_seats(self, seats):
        if not self.is_available(seats):
            raise ValueError("Not enough seats available")
        self.available_seats -= seats

    def cancel_seats(self, seats):
        self.available_seats += seats


class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    passenger_name = Column(String)
    flight_id = Column(Integer, ForeignKey('flights.id'))
    seats = Column(Integer)
    amount = Column(Float)
    status = Column(String)
    date = Column(DateTime, default=datetime.now)

    flight = relationship("Flight", back_populates="bookings")

    def cancel(self):
        if self.status == "CANCELLED":
            raise ValueError("Booking already cancelled")
        self.flight.cancel_seats(self.seats)
        self.status = "CANCELLED"



class Hotel(Base):
    __tablename__ = 'hotels'

    hotel_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    location = Column(String)
    price_per_night = Column(Float)
    available_room = Column(Integer)

    def is_available(self, rooms):
        return self.available_room >= rooms

    def book_rooms(self, rooms):
        if not self.is_available(rooms):
            raise ValueError("Not enough rooms available")
        self.available_room -= rooms
        return True

    def cancel_rooms(self, rooms):
        self.available_room += rooms
        return True

    def get_price_for_rooms(self, rooms, nights):
        return self.price_per_night * rooms * nights

    def get_hotel_info(self):
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "price_per_night": self.price_per_night,
            "available_room": self.available_room
        }
