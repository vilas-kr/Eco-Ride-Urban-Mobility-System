from vehicle import Vehicle

class ElectricScooter(Vehicle):
     
    def __init__(self, id, model, battery_percentage, max_speed_limit):
         super().__init__(id, model, battery_percentage)
         self.max_speed_limit = max_speed_limit
         
    def calculate_trip_cost(self, distance):
        # 1 base price + $0.15 per km
         return 1 + (distance * 0.15)
     
