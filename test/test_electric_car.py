import pytest
from electric_car import ElectricCar
from vehicle import Vehicle
from status import Status

class TestElectricCar:

    @pytest.fixture
    def car(self):
        return ElectricCar(1, "Tesla Model 3", 34, 5)
    
    def test_object_creation(self, car):
        '''test object creation and default values'''
        assert isinstance(car, Vehicle)
        assert type(car) is ElectricCar
        assert car.id == '1'
        assert type(car.id) is str
        assert car.battery_percentage == 34
        assert car.maintenance_status == None
        assert car.rental_price == None
        assert car.seating_capacity == 5
        
    @pytest.mark.parametrize("value", [-1, 101])
    def test_battery_exception(self, car, value):
        '''testing battery percentage exception'''
        with pytest.raises(ValueError, match="Battery percentage should be between 0 and 100"):
            car.battery_percentage = value
            
    @pytest.mark.parametrize("status", [enum for enum in Status]) 
    def test_maintenance_status(self, car, status):
        '''Test Maintanance Status'''
        car.maintenance_status = status
        assert car.maintenance_status == status
        
    @pytest.mark.parametrize("value, expected", [
        (1, 5.50),
        (5, 7.50),
        (250, 130),
    ])    
    def test_calculate_trip_cost(self, car, value, expected):
        assert car.calculate_trip_cost(value) == expected
        
    def test_to_dict(self, car):
        car.maintenance_status = Status.AVAILABLE
        car.rental_price = 2300.5
        dict = car.to_dict()
        assert dict['id'] == car.id
        assert dict['type'] == 'ElectricCar'
        assert dict['model'] == car.model
        assert dict['battery_percentage'] == car.battery_percentage
        assert dict['maintenance_status'] == car.maintenance_status.name
        assert dict['rental_price'] == car.rental_price
        assert dict['seating_capacity'] == car.seating_capacity
        
        