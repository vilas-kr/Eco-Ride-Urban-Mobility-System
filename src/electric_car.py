from vehicle import Vehicle

class ElectricCar(Vehicle):
     
    def __init__(self, id, model, battery_percentage, seating_capacity):
         super().__init__(id, model, battery_percentage)
         self.seating_capacity = seating_capacity
         
    def calculate_trip_cost(self, distance):
        # 5 base price + $0.5 per km
         return 5 + (distance * 0.5)