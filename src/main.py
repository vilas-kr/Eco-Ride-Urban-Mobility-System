from eco_ride_main import EcoRideMain

def main():
    eco = EcoRideMain()
    eco.load_hub_registry_from_json()
    eco.vehicle_maintenance_status('vilas')    
    
if __name__ == "__main__":
    main()