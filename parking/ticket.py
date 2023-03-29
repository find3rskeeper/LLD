import string
import random

class Ticket:
    def __init__(self, vehicleNumber, inTime) -> None:
        self._id = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=10))
        self.__vehicleNumber = vehicleNumber
        self.__inTime = inTime

    def getIntime(self):
        return self.__inTime
    
    def getId(self):
        return self._id

    def getVehicleNumber(self):
        return self.__vehicleNumber