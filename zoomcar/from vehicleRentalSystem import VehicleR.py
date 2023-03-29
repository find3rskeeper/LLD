from vehicleRentalSystem import VehicleRentalSystem
from car import Car
from store import Store
from user import User

cars = []
for i in range(10):
    cars.append(Car(i, 'DL10DF23'+str(i)))



store = Store(1, 'Delhi Zoomcar Store', 'Delhi', cars, cars, [])
user = User(1, 'Navneet', 'a234525safsa32423', 31, 4)
vrs = VehicleRentalSystem([user], [store])
str = vrs.getStore('Delhi')
vehicle = str.getVehicle()
reservation = str.makeReservation(vehicle, user, '12', '12', 'Delhi', 'Mumbai')
