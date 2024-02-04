from datetime import *
from checkins import CheckIn

class CheckOut(CheckIn):
    def __init__(self):
        super().__init__()
    
    def check_out(self, room_number):
        if room_number in self.rooms:
            check_out_date = date.today()
            check_in_date = self.rooms[room_number]['check_in_date']
            duration = (check_out_date - check_in_date).days
            roomtype = self.rooms[room_number]['room_type']
            if roomtype == 1:
                self.available_rooms['standart'].append(room_number)
            elif roomtype == 2:
                self.available_rooms['vip'].append(room_number)
            elif roomtype == 3:
                self.available_rooms['president'].append(room_number)
            print('--------------------------')
            print('Pleasre Hotel Receipt')
            print(f"Name:{self.rooms[room_number]['name']}\nPhone:{room_number}")
            print(f"Check-in date: {check_in_date.strftime('%d %B %Y')}")
            print(f"Check-out date: {check_out_date.strftime('%d %B %Y')}")
            print(f"No.of Days: {duration}\tPrice per day: {self.room_price[roomtype]}")
            room_bill = self.room_price[roomtype]*duration
            roomservice = self.rooms[room_number]['roomservice']
            print(f"Room bill: {room_bill}")
            print(f"Room service: {roomservice}")
            print(f"Total bill: {room_bill + roomservice}")
            del self.rooms[room_number]
        else:
            print(f"Room {room_number} is not occupied.")