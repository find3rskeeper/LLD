
from vehicle import Vehicle
from ParkingVehicleType import ParkingVehicleType

class SUV(Vehicle):
    def __init__(self, licencePlate, color=None, maker=None, model=None):
        super().__init__(ParkingVehicleType.SUV, licencePlate, color, maker, model)
