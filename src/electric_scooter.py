from vehicle import Vehicle

class ElectricScooter(Vehicle):
     
    def __init__(self, id, model, battery_percentage, max_speed_limit):
         super().__init__(id, model, battery_percentage)
         self.max_speed_limit = max_speed_limit