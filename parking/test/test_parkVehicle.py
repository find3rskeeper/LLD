import unittest
from parkinglot import *
from motorcycle import MotorCycle
from parkingLotManager import *
from car import Car
from truck import Truck

class TestParkVehicle(unittest.TestCase):
    def testMotorcyclePark(self):
        parkinglot = ParkingLot()
        parkinglot.initialiseParkingSpots()
        feeStructure ={'motorcycle': [{'startTime': 0, 'endTime': 2, 'charge': 220, 'rateType': 'flatRate'},{'startTime': 2, 'charge': 50, 'rateType': 'perHour'}]}
        plm = ParkingLotManager('Manager', parkinglot, feeStructure)
        attendant = plm.createAttendantAndAssignParkingLot('Rohan')

        vehicle = MotorCycle('DL12344')
        parkinglot.addParkingSpot('compact')
        self.assertEqual(attendant.parkVehicle(vehicle), True)

    def testCarPark(self):
        parkinglot = ParkingLot()
        parkinglot.initialiseParkingSpots()
        feeStructure ={'motorcycle': [{'startTime': 0, 'endTime': 2, 'charge': 220, 'rateType': 'flatRate'},{'startTime': 2, 'charge': 50, 'rateType': 'perHour'}]}
        plm = ParkingLotManager('Manager', parkinglot, feeStructure)
        attendant = plm.createAttendantAndAssignParkingLot('Rohan')

        vehicle = Car('DL12344')
        parkinglot.addParkingSpot('small')
        self.assertEqual(attendant.parkVehicle(vehicle), True)

    def testSUVPark(self):
        parkinglot = ParkingLot()
        parkinglot.initialiseParkingSpots()
        feeStructure ={'SUV': [{'startTime': 0, 'endTime': 2, 'charge': 220, 'rateType': 'flatRate'},{'startTime': 2, 'charge': 50, 'rateType': 'perHour'}]}
        plm = ParkingLotManager('Manager', parkinglot, feeStructure)
        attendant = plm.createAttendantAndAssignParkingLot('Rohan')

        vehicle = Car('DL12344')
        parkinglot.addParkingSpot('small')
        self.assertEqual(attendant.parkVehicle(vehicle), True)

    def testTruckPark(self):
        parkinglot = ParkingLot()
        parkinglot.initialiseParkingSpots()
        feeStructure ={'motorcycle': [{'startTime': 0, 'endTime': 2, 'charge': 220, 'rateType': 'flatRate'},{'startTime': 2, 'charge': 50, 'rateType': 'perHour'}]}
        plm = ParkingLotManager('Manager', parkinglot, feeStructure)
        attendant = plm.createAttendantAndAssignParkingLot('Rohan')

        vehicle = Truck('DL12344')
        parkinglot.addParkingSpot('large')
        self.assertEqual(attendant.parkVehicle(vehicle), True)

    def testCarParkWithoutSpot(self):
        parkinglot = ParkingLot()
        parkinglot.initialiseParkingSpots()
        feeStructure ={'car': [{'startTime': 0, 'endTime': 2, 'charge': 220, 'rateType': 'flatRate'},{'startTime': 2, 'charge': 50, 'rateType': 'perHour'}]}
        plm = ParkingLotManager('Manager', parkinglot, feeStructure)
        attendant = plm.createAttendantAndAssignParkingLot('Rohan')

        vehicle = Car('DL12344')
        parkinglot.addParkingSpot('compact')
        self.assertEqual(attendant.parkVehicle(vehicle), False)

    def testTruckParkInCompactSpot(self):
        parkinglot = ParkingLot()
        parkinglot.initialiseParkingSpots()
        feeStructure ={'truck': [{'startTime': 0, 'endTime': 2, 'charge': 220, 'rateType': 'flatRate'},{'startTime': 2, 'charge': 50, 'rateType': 'perHour'}]}
        plm = ParkingLotManager('Manager', parkinglot, feeStructure)
        attendant = plm.createAttendantAndAssignParkingLot('Rohan')

        vehicle = Truck('DL12344')
        parkinglot.addParkingSpot('compact')
        self.assertEqual(attendant.parkVehicle(vehicle), False)

    def testMotorcycleParkInLargeSpot(self):
        parkinglot = ParkingLot()
        parkinglot.initialiseParkingSpots()
        feeStructure ={'motorcycle': [{'startTime': 0, 'endTime': 2, 'charge': 220, 'rateType': 'flatRate'},{'startTime': 2, 'charge': 50, 'rateType': 'perHour'}]}
        plm = ParkingLotManager('Manager', parkinglot, feeStructure)
        attendant = plm.createAttendantAndAssignParkingLot('Rohan')

        vehicle = MotorCycle('DL12344')
        parkinglot.addParkingSpot('large')
        self.assertEqual(attendant.parkVehicle(vehicle), True)


if __name__ == '__main__':
    unittest.main()