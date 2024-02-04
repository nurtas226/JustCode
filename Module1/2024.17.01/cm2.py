class Wardrobe:
    def __init__(self):
        self.door = 'Closed'
        
    def open_door(self):
        self.door = 'Open'
        print("We open a door")

    def get_candy(self):
        if self.door == 'Closed':
            print("Door is closed!")
        else:
            print('We took candies...')
    
    def close_door(self):
        self.door = 'Closed'
        print('We closed a door')
    
    
    def __enter__(self):
        self.door = 'Open'
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.door = 'Close'

with Wardrobe() as shkafchik:
    shkafchik.get_candy()

shkafchik.get_candy()
print("End of the program!")

# shkafchik = Wardrobe()

# shkafchik.open_door()

# shkafchik.get_candy()

# shkafchik.close_door()