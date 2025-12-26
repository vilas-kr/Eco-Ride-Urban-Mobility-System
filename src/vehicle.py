from abc import ABC, abstractmethod
from status import Status

class Vehicle(ABC):
    
    def __init__(self, id: str, model: str, battery_percentage: int):
        self.id = id
        self.model = model
        self.battery_percentage = battery_percentage
        self.__maintenance_status = None
        self.__rental_price = None
        
    @property
    def maintenance_status(self):
        return self.__maintenance_status
    
    @maintenance_status.setter
    def maintenance_status(self, maintenance_status: Status):
        self.__maintenance_status = maintenance_status
        
    @property
    def rental_price(self):
        return self.__rental_price
    
    @rental_price.setter
    def rental_price(self, rental_price: float):
        self.__rental_price = rental_price
    
    @property
    def battery_percentage(self):
        return self.__battery_percentage
        
    @battery_percentage.setter
    def battery_percentage(self, battery_percentage: int):
        if 0 <= battery_percentage <= 100:
            self.__battery_percentage = battery_percentage 
        else:      
            raise ValueError("Battery percentage should be between 0 and 100")
     
    @abstractmethod   
    def calculate_trip_cost(self, distance: int):
        '''
        Parameter
        ---------
        distance : int
            total distance in kilometers
        
        Returns
        -------
        rent : float
            calculate total rent based on distance
        '''
        pass
    
    def __eq__(self, other):
        if not isinstance(other, Vehicle):
            return False
        return self.id == other.id
    
    def __lt__(self, other):
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self.model < other.model
    
    def __str__(self):
        return f"ID: {self.id}   Model: {self.model}    Battery Percentage: {self.battery_percentage}"
    
    def to_dict(self):
        return {
            'id' : self.id,
            'type' : self.__class__.__name__,
            'model' : self.model,
            'battery_percentage' : self.battery_percentage,
            'maintenance_status' : self.maintenance_status.name if self.maintenance_status else None,
            'rental_price' : self.rental_price
        }
        

