from parkingSpotType import ParkingSpotType
from parkingSpot import parkingSpot

class CompactParkingSpot(parkingSpot):
    def __init__(self, spotNumber):
        super().__init__(ParkingSpotType.COMPACT, spotNumber)

    @staticmethod
    def getParkingSlotType():
        return ParkingSpotType.COMPACT
