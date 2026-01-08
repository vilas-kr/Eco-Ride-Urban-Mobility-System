# Urban Mobility Fleet Management System

It is a system to manage fleets, vehicles and monitor vehicle maintainance status in real-time.

## Features:
1. Adding Fleet hubs.
2. Adding vehicle details to hub.
3. Viewing vehicles with their types.
4. Monitor vehicle maintainance status.
5. Sorting vehicles based on it's hub.
6. Sorting vehicles by battery percentage.
7. Save information to CSV and JSON files.
8. Retrieving information from CSV and JSON files.

## Tech stack
```
-- Language: Python
-- Tools: VSCode, Git
-- Testing: Pytest
```

## Project structure
```
Eco-Ride-Urban-Mobility-System 
|-- src/
|   |-- main.py
|   |-- eco_ride_main.py
|   |-- vehicle.py
|   |-- electric_car.py
|   |-- electric_scooter.py
|   |-- status.py
|
|-- test/
|   |-- test_eco_ride_main.py
|   |-- test_electric_car.py
|   |-- test_electric_scooter.py
|   |
|   |-- test-data/
|       |-- test_hub_data.csv
|       |-- test_hub_data.json
|
|-- data/
|   |-- hub_data.csv
|   |-- hub_data.json
|
|-- .gitignore
|-- README.md
|-- requirements.txt
```

## Installation

Clone the repository
-> git clone https://github.com/vilas-kr/Eco-Ride-Urban-Mobility-System.git

Move to project folder
-> cd Eco-Ride-Urban-Mobility-System

Install dependencies
-> pip install -r requirements.txt

Run the application
-> python main.py


## Author
```
Vilas K R
GitHub username: vilas-kr
```