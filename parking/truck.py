
from vehicle import Vehicle
from ParkingVehicleType import ParkingVehicleType

class Truck(Vehicle):
    def __init__(self, licencePlate, color=None, maker=None, model=None):
        super().__init__(ParkingVehicleType.Truck, licencePlate, color, maker, model)
