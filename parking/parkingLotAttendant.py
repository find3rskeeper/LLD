from customExceptions import NoParkingSpotException
from ticket import Ticket
from datetime import datetime
from fee import Fee
from invoice import Invoice
from parkingSpotType import ParkingSpotType
from math import ceil
from person import Person
from constants import VehicleSpotMapping

class ParkingLotAttendant(Person):
    def __init__(self, attendantId, name, parkingLot, feeStructure):
        super().__init__(name)
        self.__attendantId = attendantId
        self.__name = name
        self.__parkingLot = parkingLot
        self.feeStructure = self.createFeeStructure(feeStructure)
        self.__vehicles = {}
    
    def updateFeeStructure(self, ):
        
    def getAttendantId(self):
        return self.__attendantId

    def parkVehicle(self, vehicle):
        try:
            self.__parkingLot.parkVehicle(vehicle)
            self.__vehicles[vehicle.getLicencePlate()] = vehicle
            vehicle.ticket = Ticket(vehicle.getLicencePlate(), datetime.now())
            return True

        except NoParkingSpotException:
            print('No Parking Spot Available')
            return False


    def calculateFee(self, ticket, vehicleType):
        inTime = ticket.getIntime()
        outTime = datetime.now()
        duration = outTime - inTime
        duration = ceil(duration.seconds/3600)
        total = 0
        for serviceName in ticket.addOnservice:
            total += self.__parkinglot.calculateFee(vehicle, outTime, serviceName)

        return total + self.feeStructure[vehicleType.name.lower()].calculateFee(duration)


    def removeVehicleAndGenerateInvoice(self, vehicle):
        ticket = vehicle.ticket
        fee = self.calculateFee(ticket, vehicle.getVehicleType())
        return (fee, Invoice().generateInvoice(vehicle))


    def createFeeStructure(self, feeStructure):
        initialFee = None
        lastFee = None
        vehicleTypeFeeStructure = {}
        vehicleTypes = [vehicleType.lower() for vehicleType in VehicleSpotMapping.keys()]
        for vehicleType in feeStructure:
            if vehicleType not in vehicleTypes:
                continue
            for feeDict in feeStructure[vehicleType]:
                if not 'endTime' in feeDict:
                    duration = float('inf')
                else:
                    duration = feeDict['endTime'] - feeDict['startTime']

                fee = Fee(duration, feeDict['charge'], feeDict['rateType'])
                if not lastFee:
                    lastFee = fee
                    initialFee = fee
                else:
                    lastFee.setNextFee(fee)
                    lastFee = fee
            vehicleTypeFeeStructure[vehicleType] = initialFee
        
        return vehicleTypeFeeStructure

    def availAddOnservice(self, vehicle, serviceName):
        ticket = vehicle.ticket
        ticket.updateAddService(serviceName)
        self.__parkingLot.availAddOnService(serviceName)
        return