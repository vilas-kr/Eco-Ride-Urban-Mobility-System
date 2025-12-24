class Vehicle:
    
    def __init__(self, id, model, battery_percentage):
        self.id = id
        self.model = model
        self.battery_percentage = battery_percentage
        self.__maintenance_status = None
        self.__rental_price = None
        
    @property
    def maintenance_status(self):
        return self.__maintenance_status
    
    @maintenance_status.setter
    def maintenance_status(self, maintenance_status):
        self.__maintenance_status = maintenance_status
        
    @property
    def rental_price(self):
        return self.__rental_price
    
    @rental_price.setter
    def rental_price(self, rental_price):
        self.__rental_price = rental_price
    
    @property
    def battery_percentage(self):
        return self.__battery_percentage
        
    @battery_percentage.setter
    def battery_percentage(self, battery_percentage):
        if 0 <= battery_percentage <= 100:
            self.__battery_percentage = battery_percentage 
        else:    
            self.__battery_percentage = None  
            raise ValueError("Battery percentage should be between 0 and 100")
        
        

