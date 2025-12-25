from electric_car import ElectricCar
from electric_scooter import ElectricScooter
from vehicle import Vehicle

class EcoRideMain:
    
    hubs = {}
    def greet(self):
        print("Welcome to Eco-Ride Urban Mobility System")

    def calculate_trip_cost(self, vehicles: list[Vehicle]):
        '''
        Parameter
        ---------
        vehicles : list[Vehicle]
            list of vehicles
        
        Prints
        ------
        vehicle model and total trip cost by taking distance as input
        '''
        for i in vehicles:
            n = int(input("Enter trip distance : "))
            print(f'{i.model} : {i.calculate_trip_cost(n)}')
    
    def add_hub(self, hub_name: str):
        """
        Adds a hub to the EcoRide hubs registry.

        Parameters
        ----------
        hub_name : str
            The name of the hub to be added.

        Returns
        -------
        bool
            True
                If the hub name is successfully added to the dictionary.
            False
                If the hub name already exists in the dictionary.
        """
        if hub_name not in EcoRideMain.hubs:
            EcoRideMain.hubs[hub_name] = []
            return True
        return False
    
    def add_vehicle(self, hub_name: str, vehicle: Vehicle):
        """
        Adds a vehicle to the specified hub registry.

        Parameters
        ----------
        hub_name : str
            The name of the hub to which the vehicle will be added.

        vehicle : Vehicle
            The vehicle object to be added to the hub.

        Returns
        -------
        bool
            True
                If the vehicle is successfully added to the hub.
            False
                If the specified hub does not exist in the registry or if vehicle id is not.
        """
        if hub_name in EcoRideMain.hubs:
            if not any([vehicle == other for other in EcoRideMain.hubs[hub_name]]):
                EcoRideMain.hubs[hub_name].append(vehicle)
                return True
            print("Duplicate vehicle ID detected")
        return False 
    
    def check_hub(self, hub_name: str):
        '''
        Check hub name present in the hub registry
        
        Parameter
        ---------
        hub_name : str
            The name of the hun you want to check in hub registry
            
        Returns
        -------
        bool
            True
                if hub name present in the hub registry
            False
                if hub name not present in the hub registry
        '''
        if hub_name in EcoRideMain.hubs:
            return True
        return False
    


     
             
                            
                    
                
    

    
    
            
            
        
        
            



        