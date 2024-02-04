from checkouts import CheckOut

class Occupied(CheckOut):
    def __init__(self):
        super().__init__()
    
    def display_occupied(self):
        if not self.rooms:
            print("No rooms are occupied at the moment.")
        else:
            print("Ocupied rooms: ")
            print("_________________________________")
            print("Room no. Name Phone")
            print("_________________________________")
            for room_number, details in self.rooms.items():
                print(room_number, '\t',details['name'], '\t', details['phone'])
                