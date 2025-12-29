from vehicle import Vehicle

class ElectricCar(Vehicle):
     
    def __init__(self, id: str, model: str, battery_percentage: int, seating_capacity: int):
         super().__init__(id, model, battery_percentage)
         self.seating_capacity = seating_capacity
         
    def calculate_trip_cost(self, distance: int):
        # 5 base price + $0.5 per km
         return 5 + (distance * 0.5)
     
    def to_dict(self):
        return {
            'id' : self.id,
            'type' : self.__class__.__name__,
            'model' : self.model,
            'battery_percentage' : self.battery_percentage,
            'maintenance_status' : self.maintenance_status.name if self.maintenance_status else None,
            'rental_price' : self.rental_price,
            'seating_capacity' : self.seating_capacity
        }