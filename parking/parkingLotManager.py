from parkingLotAttendant import ParkingLotAttendant
from person import Person

class ParkingLotManager():
    def __init__(self, person, parkingLot, __feeStructure):
        self.person = person
        self.__parkingLot = parkingLot
        self.attendants = {}
        self.__feeStructure = __feeStructure
    
    #Create attendant and assign parking spot to the attendant
    def createAttendantAndAssignParkingLot(self, attendantName = None):
        if not attendantName:
            attendantName = 'Attendant ' + len(self.attendants) + 1

        attendant = ParkingLotAttendant(len(self.attendants) + 1, attendantName, self.__parkingLot, self.__feeStructure)
        self.attendants[attendant.getAttendantId()] = attendant
        return attendant