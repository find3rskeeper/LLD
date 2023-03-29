
from vehicle import Vehicle
from ParkingVehicleType import ParkingVehicleType

class Car(Vehicle):
    def __init__(self, licencePlate, color=None, maker=None, model=None):
        super().__init__(ParkingVehicleType.Car, licencePlate, color, maker, model)
