import string
import unittest
from parkinglot import *
from motorcycle import MotorCycle
from parkingLotManager import *
from car import Car
from ticket import Ticket
from truck import Truck
from datetime import datetime, timedelta

class TestParkVehicle(unittest.TestCase):
    def testMotorcycleUnpark(self):
        parkinglot = ParkingLot()
        parkinglot.initialiseParkingSpots()
        feeStructure ={'motorcycle': [{'startTime': 0, 'endTime': 2, 'charge': 220, 'rateType': 'flatRate'},{'startTime': 2, 'charge': 50, 'rateType': 'perHour'}]}
        plm = ParkingLotManager('Manager', parkinglot, feeStructure)
        attendant = plm.createAttendantAndAssignParkingLot('Rohan')

        vehicle = MotorCycle('DL12344')
        parkinglot.addParkingSpot('compact')
        attendant.parkVehicle(vehicle)
        (parkingCharge, invoice) = attendant.removeVehicleAndGenerateInvoice(vehicle)
        self.assertEqual(parkingCharge, 220)
        self.assertEqual(isinstance(invoice, str), True)

    def testTicketFee(self):
        parkinglot = ParkingLot()
        parkinglot.initialiseParkingSpots()
        feeStructure = {'motorcycle': [
                                        {'startTime': 0, 'endTime': 2, 'charge': 220, 'rateType': 'flatRate'},
                                        {'startTime': 2, 'charge': 50, 'rateType': 'perHour'}
                                    ]
                        }
        plm = ParkingLotManager('Manager', parkinglot, feeStructure)
        attendant = plm.createAttendantAndAssignParkingLot('Rohan')

        intime = datetime.now() - timedelta(hours = 5)
        ticket = Ticket('DL12344', intime)
        fee = attendant.calculateFee(ticket, ParkingVehicleType.MotorCycle)
        self.assertEqual(fee, 420)

if __name__ == '__main__':
    unittest.main()