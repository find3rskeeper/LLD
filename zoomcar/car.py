from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, vehicleId, vehicleNo) -> None:
        super().__init__(vehicleId, vehicleNo, 4)