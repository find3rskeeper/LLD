from vehicle import Vehicle
from ParkingVehicleType import ParkingVehicleType

class MotorCycle(Vehicle):
    def __init__(self, licencePlate, color=None, maker=None, model=None):
        super().__init__(ParkingVehicleType.MotorCycle, licencePlate, color, maker, model)
