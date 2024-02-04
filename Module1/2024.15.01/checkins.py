from datetime import date
from services import Service

class CheckIn(Service):
    def __init__(self):
        super().__init__()
        self.available_rooms = {'standart':[1,2,3], 'vip':[11,12,13], 'president':[100]}
        self.room_price = {1:15000, 2:30000, 3:80000}
        
    def check_in(self, name, phone):
        roomtype = int(input('Room types: \n1. Standart \n2. VIP \n3. President\nSelect a room type: '))
        
        if roomtype == 1:
            if self.available_rooms['standart']:
                room_number = self.available_rooms['standart'].pop(0)
            else:
                print("Sorry, standart room not available.")
                return
        elif roomtype == 2:
            if self.available_rooms['vip']:
                room_number = self.available_rooms['vip'].pop(0)
            else:
                print("Sorry, VIP room not available.")
                return
        elif roomtype == 3:
            if self.available_rooms['president']:
                room_number = self.available_rooms['president'].pop(0)
            else:
                print("Sorry, president room not available.")
                return
        else:
            print("Choose a valid room type.")
        
        d,m,y = map(int,input("Enter check-in date in date,month,year(xx xx xxxx): ").split())
        check_in = date(y,m,d)
        self.rooms[room_number] = {
            'name':name,
            'phone': phone,
            'check_in_date':check_in,
            'room_type': roomtype,
            'roomservice':0
        }
        print('----------------------')
        print(f"{name} checked-in to room: {room_number} on {check_in} ")
        
        
# h = CheckIn()
# h.check_in('ASDGSAD', 34124)