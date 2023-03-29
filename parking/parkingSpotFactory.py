from constants import ParkingSpotMapping

class ParkingSpotFactory:
    def __init__(self):
        pass
    @staticmethod
    def createParkingSpot(parkingSpotType, spotNumber):
        if parkingSpotType not in ParkingSpotMapping:
            return None
        
        return ParkingSpotMapping[parkingSpotType](spotNumber)
