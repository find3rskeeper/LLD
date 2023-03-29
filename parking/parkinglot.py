
from datetime import datetime
from queue import PriorityQueue
from ParkingVehicleType import ParkingVehicleType
from parkingSpotType import ParkingSpotType
from parkingSpotFactory import ParkingSpotFactory
from constants import VehicleSpotMapping, addOnServices
from customExceptions import NoParkingSpotException, NoVehicleFoundException
from largeParkingSpot import LargeParkingSpot
from vehicleCleaning import VehicleCleaning, ChargingFacility

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
            

class ParkingLot(metaclass=Singleton):
    
    #Initialize function to set initial variables
    #This function can take a list of parking slot details to be initialized parking slots in bulk
    def initialiseParkingSpots(self):
        self.availableParkingSpots = {}
        for spotType in ParkingSpotType._member_names_:
            self.availableParkingSpots[spotType.lower()] = PriorityQueue()
            self.__dict__[spotType.lower()+'_count'] = 0


        self.addOnServices = {'cleaning': VehicleCleaning, 'charging': ChargingFacility}
    
        self.parkedVehicles = {}

    #Basic function to add parking slot of specific type
    def addParkingSpot(self, spotType):
        spotTypeCountKey = spotType.lower() + '_count'
        self.__dict__[spotTypeCountKey] = self.__dict__[spotTypeCountKey] + 1

        spotTypeCount = self.__dict__[spotTypeCountKey]
        parkingSpot = ParkingSpotFactory.createParkingSpot(spotType, spotTypeCount)
        self.availableParkingSpots[spotType.lower()].put((spotTypeCount, parkingSpot))


    def removeParkingSpot(self):
        pass
    
    #Function to take care of parking a vehicle
    def parkVehicle(self, vehicle):
        parkingVehicleType = vehicle.getVehicleType()
        (isSpotAvailable, parkingSpotTuple) = self.getSpot(parkingVehicleType)
        if not isSpotAvailable:
            raise NoParkingSpotException
        
        parkingSpot = parkingSpotTuple[1]
        isVehicleParked = parkingSpot.occupySpot(vehicle)
        self.parkedVehicles[vehicle.getLicencePlate()] = parkingSpot
        return isVehicleParked

    
    def getSpot(self, parkingVehicleType):
        parkingSpotType = None
        if parkingVehicleType.name not in VehicleSpotMapping:
            parkingSpotType = ParkingSpotType.LARGE
        else:
            parkingSpotType = VehicleSpotMapping[parkingVehicleType.name][0]
        
        return self.getParkingSpot(parkingSpotType)

    #inner function to check if a parking spot is available or not
    def getParkingSpot(self, parkingSpotType):
        parkingSpotTypesToCheck = []
        #Fetching all parking spot type above parkingSpotType required
        for parkingSpot in ParkingSpotType:
            if parkingSpot.value >= parkingSpotType.value:
                parkingSpotTypesToCheck.append((parkingSpot.value, parkingSpot.name))

        parkingSpotTypesToCheck.sort()
        #Checking if a parking spot is available or not. Returning from Priority queue
        for parkingSpotType in parkingSpotTypesToCheck:
            parkingSpotkey = parkingSpotType[1].lower()
            availableSpotPQ = self.availableParkingSpots[parkingSpotkey]
            availableSpots = availableSpotPQ.qsize()
            if availableSpots:
                return (True, availableSpotPQ.get())
        
        return (False, None)

    #Function to remove vehicleand free parking spot
    def removeVehicle(self, vehicle):
        licencePlate = vehicle.getLicencePlate()
        if licencePlate not in self.parkedVehicles:
            raise NoVehicleFoundException
        
        parkingSpot = self.parkedVehicles[licencePlate]
        if not parkingSpot:
            return None

        parkingSpot.freeSpot()
        parkingSpotType = parkingSpot.getParkingSlotType().name.lower()
        self.availableParkingSpots[parkingSpotType].put((parkingSpot.getParkingSpotNumber(), parkingSpot))
        return parkingSpot

        
    def availAddOnService(self, vehicle, serviceName):
        return self.addOnServices[serviceName].avail(vehicle)