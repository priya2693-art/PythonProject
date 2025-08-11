class Hotel:
     def __init__(self,hotel_id,name,location,price_per_night,available_room):
         self.hotel_id= hotel_id
         self.name= name
         self.location= location
         self.price_per_night= price_per_night
         self.available_room= available_room


     def is_available(self,rooms):
         return self.available_room>= rooms


     def book_rooms(self,rooms):
         if not self.is_available(rooms):
             raise ValueError("Not enough rooms available")
         self.available_room -=rooms
         return True

     def cancel_rooms(self,rooms):
         self.available_room += rooms
         return True

     def get_price_for_rooms(self,rooms,nights):
         return self.price_per_night *rooms *nights

     def get_hotel_info(self):
         return{
             "hotel_id": self.hotel_id,
             "name": self.name,
             "location": self.location,
             "price_per_night":self.price_per_night,
             "available_room":self.available_room
         }
