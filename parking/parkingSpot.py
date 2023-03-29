class parkingSpot:
    def __init__(self, parkingSlotType, spotNumber = -1):
        #static Variables
        self.__parkingSlotType  = parkingSlotType

        #object Variables
        self.__free = True
        self.vehicle = None
        self.__spotNumber = spotNumber

    def isFree(self):
        return self.__free

    def occupySpot(self, vehicle):
        self.vehicle = vehicle
        self.__free = False
        return True
 
    def freeSpot(self):
        self.vehicle = None
        self.__free = True
        return True
    
    def getParkingSpotType(self):
        return self.__parkingSlotType
    
    def getParkingSpotNumber(self):
        return self.__spotNumber
