from abc import ABC

class Vehicle(ABC):
    def __init__(self, vehicleType, licencePlate, color = None, maker = None, model= None):
        self.__vehicleType = vehicleType
        self.__licencePlate = licencePlate
        self.__color = color
        self.__maker = maker
        self.__model = model
    
    def getVehicleType(self):
        return self.__vehicleType
    
    def getLicencePlate(self):
        return self.__licencePlate
