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
                If the specified hub does not exist in the registry.
        """
        if hub_name in EcoRideMain.hubs:
            EcoRideMain.hubs[hub_name].append(vehicle)
            return True
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
     
#Menu based interface 
def add_vehicle_menu(eco_ride):
    hub_name = input("Enter hub name : ")
    while not eco_ride.check_hub(hub_name):
        hub_name = input("Invalid hub name\nEnter valid hub name : ")
    while True:
        vehicle_type = input("\nEnter 1 car \nEnter 2 scooty \nEnter type of vehicle : ")
        match vehicle_type:
            case '1':
                #taking input from the user for object creation
                id = input("Enter vehicle id : ")
                model = input("Enter model : ")
                battery_percentage = int(input("Enter vehicle battery percentage : "))
                maintenance_status = input("Enter maintenance status : ")
                rental_price = float(input("Enter Rental price : "))
                seat_capacity = int(input("Enter number of seats : "))
                
                #initialize car object
                try:
                    car = ElectricCar(id, model, battery_percentage, seat_capacity)
                except Exception as e:
                    print(e)
                    continue
                car.maintenance_status = maintenance_status
                car.rental_price = rental_price
                
                #adding object to the hub
                eco_ride.add_vehicle(hub_name, car)
                
            case '2':
                #taking input from the user for object creation
                id = input("Enter vehicle id : ")
                model = input("Enter model : ")
                battery_percentage = int(input("Enter vehicle battery percentage : "))
                maintenance_status = input("Enter maintenance status : ")
                rental_price = float(input("Enter Rental price : "))
                max_speed = int(input("Enter maximum speed limit : "))
                
                #initialize scooty object
                try:
                    scooty = ElectricScooter(id, model, battery_percentage, max_speed)
                except Exception as e:
                    print(e)
                    continue
                scooty.maintenance_status = maintenance_status
                scooty.rental_price = rental_price
                
                #adding object to the hub
                eco_ride.add_vehicle(hub_name, scooty)
    
            
            case _ :
                print("Invalid choice")
            
        #check if user wants to add more vehicle
        if input("Do you want to add more vehicle (y/n) : ") == 'n':
            break
        
def main():
    eco_ride = EcoRideMain()
    while True:
        choice = input("\nEnter 1 add new hub \nEnter 2 add vehicle to existing hub \nEnter 3 exit\nEnter your choice : ")
        match choice:
            case '1': 
                hub_name = input("Enter hub name : ")
                if not eco_ride.add_hub(hub_name):
                    print("Hub name is already present")
            case '2':
                add_vehicle_menu(eco_ride)
            
            case '3':
                print(eco_ride.hubs)
                return
            
            case _ :
                print("Invalid choice")
            
if __name__ == "__main__":
    main()           
                        
                            
                    
                
    

    
    
            
            
        
        
            



        