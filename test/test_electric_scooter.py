import pytest
from electric_scooter import ElectricScooter
from vehicle import Vehicle
from status import Status

class TestElectricScooter:

    @pytest.fixture
    def scooter(self):
        return ElectricScooter(7, "Activa", 87, 80)
    
    def test_object_creation(self, scooter):
        '''test object creation and default values'''
        assert isinstance(scooter, Vehicle)
        assert type(scooter) is ElectricScooter
        assert scooter.id == '7'
        assert scooter.battery_percentage == 87
        assert scooter.maintenance_status == None
        assert scooter.rental_price == None
        assert scooter.max_speed_limit == 80
        
    @pytest.mark.parametrize("value", [-1, 101])
    def test_battery_exception(self, scooter, value):
        '''testing battery percentage exception'''
        with pytest.raises(ValueError, match="Battery percentage should be between 0 and 100"):
            scooter.battery_percentage = value
            
    @pytest.mark.parametrize("status", [enum for enum in Status]) 
    def test_maintenance_status(self, scooter, status):
        '''Test Maintanance Status'''
        scooter.maintenance_status = status
        assert scooter.maintenance_status == status
        
    @pytest.mark.parametrize("value, expected", [
        (1, 1.15),
        (5, 1.75),
        (250, 38.5),
    ])    
    def test_calculate_trip_cost(self, scooter, value, expected):
        assert scooter.calculate_trip_cost(value) == expected
        
    def test_to_dict(self, scooter):
        scooter.maintenance_status = Status.ON_TRIP
        scooter.rental_price = 1200.80
        dict = scooter.to_dict()
        assert dict['id'] == scooter.id
        assert dict['type'] == 'ElectricScooter'
        assert dict['model'] == scooter.model
        assert dict['battery_percentage'] == scooter.battery_percentage
        assert dict['maintenance_status'] == scooter.maintenance_status.name
        assert dict['rental_price'] == scooter.rental_price
        assert dict['max_speed_limit'] == scooter.max_speed_limit
        
        
        
        