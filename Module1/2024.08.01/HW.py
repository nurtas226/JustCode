class Car:
    total_cars = 0
    
    def __init__(self, make, model, year, color):
        self.make = make 
        self.model = model 
        self.year = year 
        self.color = color 
        
        Car.total_cars += 1
    
    def car_info(self):
        print(f"({self.make}, {self.model}, {self.year}), Color: {self.color}")
    
car1 = Car("BMW", "X5", 2022, "Black")
car2 = Car("BMW", "X6", 2020, "White")
car3 = Car("BMW", "M5", 2018, "Blue")

car1.car_info()
car2.car_info()
car3.car_info()

print(f"Total cars: {Car.total_cars}\n")

class ElectricCar(Car):
    def __init__(self, make, model, year, color, battery_capacity):
        super().__init__(make, model, year, color)
        self.battery_capacity = battery_capacity
    
    def car_info(self):
        print(f"({self.make}, {self.model}, {self.year}), (Color: {self.color}), (Battery capacity: {self.battery_capacity})")
        
electric_car1 = ElectricCar("BMW", "i4", 2024, "White", 282)
electric_car2 = ElectricCar("BMW", "i7", 2024, "Grey", 650)

electric_car1.car_info()
electric_car2.car_info()

print(f"Total Cars: {Car.total_cars}")