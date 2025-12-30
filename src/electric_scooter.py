from vehicle import Vehicle

class ElectricScooter(Vehicle):
     
    def __init__(self, id: str, model: str, battery_percentage: int, max_speed_limit: int):
         super().__init__(id, model, battery_percentage)
         self.max_speed_limit = int(max_speed_limit)
         
    def calculate_trip_cost(self, distance: int):
        # 1 base price + $0.15 per km
         return 1 + (distance * 0.15)
     
    def to_dict(self):
        return {
            'id' : self.id,
            'type' : self.__class__.__name__,
            'model' : self.model,
            'battery_percentage' : self.battery_percentage,
            'maintenance_status' : self.maintenance_status.name if self.maintenance_status else None,
            'rental_price' : self.rental_price,
            'max_speed_limit' : self.max_speed_limit
        }