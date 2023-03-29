from parkingSpotType import ParkingSpotType
from parkingSpot import parkingSpot

class LargeParkingSpot(parkingSpot):
    def __init__(self, spotNumber):
        super().__init__(ParkingSpotType.LARGE, spotNumber)

    @staticmethod
    def getParkingSlotType():
        return ParkingSpotType.LARGE
