import pytest
import os
import csv

from eco_ride_main import EcoRideMain
from electric_car import ElectricCar
from electric_scooter import ElectricScooter
from status import Status


class TestEcoRideMain:
    
    @pytest.fixture
    def b1(self):
        b1 = ElectricScooter(2003, "Activa", 99, 120)
        b1.maintenance_status = Status.AVAILABLE
        b1.rental_price = 230
        return b1
    
    @pytest.fixture  
    def b2(self):  
        b2 = ElectricCar(2001, "Tesla Model 3", 50, 5)
        b2.maintenance_status = Status.AVAILABLE
        b2.rental_price = 500
        return b2

    @pytest.fixture
    def b3(self):
        b3 = ElectricScooter(2004, 'Access 125', 81, 115)
        b3.maintenance_status = Status.UNDER_MAINTENANCE
        b3.rental_price = 180
        return b3
        
    @pytest.fixture    
    def b4(self):
        b4 = ElectricCar(2002, 'Creta', 78, 5)
        b4.maintenance_status = Status.ON_TRIP
        b4.rental_price = 600
        return b4
    
    @pytest.fixture
    def h1(self):
        h1 = ElectricCar(1901, 'Lamborgini', 98, 4)
        h1.maintenance_status = Status.AVAILABLE
        h1.rental_price = 1300
        return h1
        
    @pytest.fixture
    def h2(self):
        h2 = ElectricScooter(1903, 'R15 V4', 88, 155)
        h2.maintenance_status = Status.ON_TRIP
        h2.rental_price = 350
        return h2
        
    @pytest.fixture
    def h3(self):
        h3 = ElectricScooter(1902, 'Ola S1 Pro', 60, 90)
        h3.maintenance_status = Status.UNDER_MAINTENANCE
        h3.rental_price = 160
        return h3
    
    @pytest.fixture
    def m1(self):
        m1 = ElectricCar(3404, 'MG ZS EV', 95, 5)
        m1.maintenance_status = Status.AVAILABLE
        m1.rental_price = 550
        return m1
    
    @pytest.fixture
    def d1(self):
        d1 = ElectricScooter(9190, 'Access 125', 88, 120)
        d1.maintenance_status = Status.AVAILABLE
        d1.rental_price = 150
        return d1
     
    @pytest.fixture
    def eco(self, b1, b2, b3, b4, h1, h2, h3, m1, d1):
        EcoRideMain.hubs = {
            "Bangalore": [ b1, b2, b3, b4 ],
            "Hubli": [ h1, h2, h3 ],
            "Mysore": [ m1 ],
            "Davangere": [ d1 ]
        }
        return EcoRideMain()
    
    @pytest.fixture
    def eco_empty(self):
        return EcoRideMain()
    
    def test_add_hub(self, eco):
        assert eco.add_hub("Hassan") == True
        #duplicate hub name
        assert eco.add_hub("Hassan") == False
         
    def test_add_vehicle(self, eco, capsys):
        assert eco.add_vehicle('Bangalore', ElectricCar(1, 'Verna', 78, 7)) == True
        #duplicate id check
        assert eco.add_vehicle('Bangalore', ElectricCar(1, 'BMW', 98, 5)) == False
        reader = capsys.readouterr().out
        assert 'Duplicate vehicle ID detected\n' == reader
        
    def test_check_hub(self, eco):
        assert eco.check_hub('Bangalore') == True
        assert eco.check_hub('hassan') == False
        
    def test_search_by_battery(self, eco, b1, b3):
        # Hub not present
        assert eco.search_by_battery('Hassan') == []
        assert eco.search_by_battery('Bangalore') == [b1, b3]
        
    def test_group_vehicles_by_type(self, eco, b1, b2, b3, b4, h1, h2, h3, m1, d1):
        assert eco.group_vehicles_by_type() == {
            'CAR': [b2, b4, h1, m1],
            'SCOOTER' : [b1, b3, h2, h3, d1]
        }
        # empty dictionary
        EcoRideMain.hubs = {}
        assert eco.group_vehicles_by_type() == {'CAR': [], 'SCOOTER':[]}
        
    def test_vehicle_maintenance_status(self, eco, capsys):
        eco.vehicle_maintenance_status('Bangalore')
        reader = capsys.readouterr().out
        assert reader == f'Maintenance status of Bangalore hub as below\nAVAILABLE : 2\nON_TRIP : 1\nUNDER_MAINTENANCE : 1\n'
        # Invalid hub
        eco.vehicle_maintenance_status('Hassan') == None
          
    def test_sort_vehicle(self, eco, b1, b2, b3, b4):
        assert eco.sort_vehicle('Bangalore') == True
        assert EcoRideMain.hubs['Bangalore'] == [b3, b1, b4, b2]
        
        # Invalid hub name
        assert eco.sort_vehicle('Hassan') == False
         
    def test_sort_vehicle_by_battery(self, eco, b1, b2, b3, b4):
        eco.sort_vehicle_by_battery('Bangalore')
        assert EcoRideMain.hubs['Bangalore'] == [b1, b3, b4, b2]
        
    def test_save_hub_registry_to_csv(self, eco):
        eco.save_hub_registry_to_csv('test_hub_data.csv')
        assert os.path.exists('test_hub_data.csv')
    
    def test_csv_data(self):
        with open('test_hub_data.csv', 'r') as f:
            assert f.readline() == f"hub_name,id,type,model,battery_percentage,maintenance_status,rental_price,extra\n"
            for hub in EcoRideMain.hubs:
                for v in EcoRideMain.hubs[hub]:
                    assert f.readline() == f'{hub},{v.id},{v.__class__.__name__},{v.model},{v.battery_percentage},{v.maintenance_status.name if v.maintenance_status else None},{v.rental_price},{v.seating_capacity if isinstance(v, ElectricCar) else v.max_speed_limit}\n'
                    
    def test_load_hub_registry_from_csv(self, eco_empty):
        assert os.path.exists("test_hub_data.csv")
        eco_empty.load_hub_registry_from_csv('test_hub_data.csv')
        with open('test_hub_data.csv', 'r') as f:
            details = csv.DictReader(f)
            for hub_name in EcoRideMain.hubs:
                for v, vehicleDetails in zip(EcoRideMain.hubs[hub_name], details):
                    assert hub_name == vehicleDetails['hub_name']
                    assert v.id == str(vehicleDetails['id'])
                    assert v.model == vehicleDetails['model']
                    assert v.battery_percentage == int(vehicleDetails['battery_percentage'])
                    assert v.maintenance_status == Status[vehicleDetails['maintenance_status']]
                    assert v.rental_price == float(vehicleDetails['rental_price'])
                    assert v.__class__.__name__ == vehicleDetails['type']
                    assert v.seating_capacity if isinstance(v, ElectricCar) else v.max_speed_limit == int(vehicleDetails['extra'])
            
            
            
        
        
    
        
        
    