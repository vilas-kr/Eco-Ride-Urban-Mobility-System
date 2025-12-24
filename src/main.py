from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class EcoRideMain:
    
    def greet(self):
        print("Welcome to Eco-Ride Urban Mobility System")

e1 = ElectricScooter(1, "pep+", 30, 85)
e2 = ElectricScooter(2, "ola", 50, 120)
e3 = ElectricScooter(3, "simple one", 90, 100)
c1 = ElectricCar(1,"verna", 10, 5)
c2 = ElectricCar(2, "BMW", 38, 7)
c3 = ElectricCar(3, "swift", 99, 4)
vehicles = [e1, c1, e2, c2, e3, c3]
for i in vehicles:
    n = int(input("Enter trip distance : "))
    print(f'{i.model} : {i.calculate_trip_cost(n)}')

        