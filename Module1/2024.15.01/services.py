class Service:
    def __init__(self):
        self.rooms = {}
        
    def room_service(self, room_number):
        
        if room_number in self.rooms:
            print("****** Pleasure Restaurant Menu ******")
            print("1. Tea: 500tg\n2. Coffee: 500tg\n3. Dessert: 1000tg\n4. Breakfast: 1500tg\n5. Exit")
            while 1:
                selection = int(input("Select your choice: "))
                if selection == 1:
                    q = int(input("Enter the quantity: "))
                    self.rooms[room_number]['roomservice']+=500*q
                    
                elif selection == 2:
                    q = int(input("Enter the quantity: "))
                    self.rooms[room_number]['roomservice']+=500*q
                    
                elif selection == 3:
                    q = int(input("Enter the quantity: "))
                    self.rooms[room_number]['roomservice']+=1000*q
                    
                elif selection == 4:
                    q = int(input("Enter the quantity: "))
                    self.rooms[room_number]['roomservice']+=1500*q
                elif selection == 5:
                    break
                else:
                    print("Invalid option")
            print("Room service: ", self.rooms[room_number]['roomservice'],"\n")
        else:
            print("Invalid room number")   