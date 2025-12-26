import csv
from electric_car import ElectricCar
from electric_scooter import ElectricScooter
from vehicle import Vehicle
from status import Status


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
                self.sort_vehicle_by_battery(hub_name)
                return True
            print("Duplicate vehicle ID detected")
        return False 
    
    def check_hub(self, hub_name: str):
        '''
        Check hub name present in the hub registry
        
        Parameter
        ---------
        hub_name : str
            The name of the hub you want to check in hubs registry
            
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
    
    def search_by_battery(self, hub_name: str):
        '''
        Returns vehicles with battery percentage greater than 80
        from the specified hub
        
        Parameter
        ---------
        hub_name: str
            The name of the hub you want to search in hubs registry
        
        Returns
        -------
        vehicles : list of Vehicles
            vehicles which have more than 80 percent battery in the specified hub
        '''
        if not self.check_hub(hub_name):
            return []
        return list(filter(lambda obj : obj.battery_percentage > 80, EcoRideMain.hubs[hub_name]))
        
    def group_vehicles_by_type(self):
        """
        Groups all vehicles across hubs by their type.

        Returns
        -------
        dict
            Mapping of vehicle type to list of vehicles.
            Example:
            {
                "CAR": [...],
                "SCOOTER": [...]
            }
        """
        vehicle_type = {
            "CAR": [],
            "SCOOTER": []
        }       
        for vehicles in EcoRideMain.hubs.values():
            for vehicle in vehicles:
                if isinstance(vehicle, ElectricCar):
                    vehicle_type["CAR"].append(vehicle)
                elif isinstance(vehicle, ElectricScooter):
                    vehicle_type["SCOOTER"].append(vehicle)
        
        return vehicle_type

    def vehicle_maintenance_status(self, hub_name: str):
        '''
        Count status of all vehicles in the specified hub
        
        Parameter
        ---------
        hub_name : str
            The name of the hub to which the vehicle status to be checked.
        
        Prints
        ------
            Summary of all vehicle maintenance status in the specified hub   
        '''
        #check for hub existance
        if not self.check_hub:
            return
        
        maintenance_status = {}
        #initialize dictionary
        for status in Status:
            maintenance_status[status.name] = 0
            
        #Count vehicles by there maintenance status
        for vehicle in EcoRideMain.hubs[hub_name]:
            maintenance_status[vehicle.maintenance_status.name] += 1
        
        #print summary
        print(f"Maintenance status of {hub_name} hub as below")
        for status, count in maintenance_status.items():
            print(f"{status} : {count}")
        
    def sort_vehicle(self, hub_name: str):
        '''
        Sorted vehicles by there name in ascending order in specified hub
        
        Parameter
        ---------
        hub_name: str
            The name of the hub to which the vehicle to be sort.
        
        Returns
        -------
        bool
            True
                Successfull sort
            False
                Unsuccessfull sort
        '''
        #Check existance of hub
        if not self.check_hub(hub_name):
            return False
        EcoRideMain.hubs[hub_name].sort()
        return True
    
    def sort_vehicle_by_battery(self, hub_name: str):
        '''
        Sort vehicle by battery percentage in decending order in the specified hub
        
        Parameter
        ---------
        hub_name: str
            Specify the hub name to be sort
        
        Modify
        ------
            sort the list of Vehicles by battery percentage
        '''
        #Check hub existance
        if not self.check_hub(hub_name):
            return
        EcoRideMain.hubs[hub_name].sort(key = lambda vehicle: vehicle.battery_percentage , reverse = True)
        
    def save_hubs_data_to_csv(self):
        '''
        Store hubs data into csv file
        '''
        with open("hubs_data.csv", "w", newline="") as f:
            writer = csv.writer(f)
            #header
            writer.writerow([
                "hub_name", "vehicle_id", "vehicle_type",
                "model", "battery_percentage", "maintenance_status", "rental_price", "extra"
            ])

            for hub, vehicles in EcoRideMain.hubs.items():
                for v in vehicles:
                    writer.writerow([
                        hub,
                        v.id,
                        v.__class__.__name__,
                        v.model,
                        v.battery_percentage,
                        v.maintenance_status.name if v.maintenance_status else "UNKNOWN",
                        v.rental_price,
                        v.seating_capacity if isinstance(v, ElectricCar) else v.max_speed_limit
                    ])
            
    def load_hubs_data_from_csv(self):
        '''
        Store csv file data back to hubs registory by creating objects
        '''
        try:
            with open('hubs_data.csv', mode="r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    hub_name = row['hub_name']

                    # create hub if not exists
                    if hub_name not in EcoRideMain.hubs:
                        EcoRideMain.hubs[hub_name] = []

                    vehicle_type = row["vehicle_type"]
                    vehicle_id = row["vehicle_id"]
                    model = row["model"]
                    battery = int(row["battery_percentage"])
                    status = Status[row["maintenance_status"]]
                    rental_price = row['rental_price']


                    # recreate correct object
                    if vehicle_type == "ElectricCar":
                        vehicle = ElectricCar(vehicle_id, model, battery, row['extra'])
                    elif vehicle_type == "ElectricScooter":
                        vehicle = ElectricScooter(vehicle_id, model, battery, row['extra'])
                    else:
                        continue
                    vehicle.maintenance_status = status
                    vehicle.rental_price = rental_price
                    self.add_vehicle(hub_name, vehicle)

        except FileNotFoundError:
            print("No existing fleet data found. Starting fresh.")
              

                    
                
    

    
    
            
            
        
        
            



        