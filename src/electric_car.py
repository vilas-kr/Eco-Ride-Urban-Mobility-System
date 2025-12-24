from vehicle import Vehicle

class ElectricCar(Vehicle):
     
    def __init__(self, id, model, battery_percentage, seating_capacity):
         super().__init__(id, model, battery_percentage)
         self.seating_capacity = seating_capacity