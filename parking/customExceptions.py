
class NoParkingSpotException(Exception):
    def __init__(self, message='No Parking Spot'):
        super(NoParkingSpotException, self).__init__(message)

class NoVehicleFoundException(Exception):
    def __init__(self, message='No Vehicle Found'):
        super(NoParkingSpotException, self).__init__(message)