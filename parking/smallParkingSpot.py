from parkingSpotType import ParkingSpotType
from parkingSpot import parkingSpot

class SmallParkingSpot(parkingSpot):
    def __init__(self, spotNumber):
        super().__init__(ParkingSpotType.SMALL, spotNumber)

    @staticmethod
    def getParkingSlotType():
        return ParkingSpotType.SMALL
