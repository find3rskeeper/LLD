from reservation import Reservation
from reservationStatus import RESERVATIONSTATUS
from vehicleInventory import VehicleInventory

class Store:
    def __init__(self, id, name, location, vehicles, freeVehicles, reservations) -> None:
        self.id = id
        self.name = name
        self.location = location
        self.vehicleInventory = VehicleInventory(vehicles, freeVehicles)
        self.reservations = {}
        for reservation in reservations:
            self.reservations[reservation.id] = reservation
    
    def makeReservation(self, vehicle, person, pickupTime, dropTime, pickupLocation, dropLocation):
        reservation = Reservation(len(self.reservations), vehicle, person, pickupTime, dropTime, pickupLocation, dropLocation, RESERVATIONSTATUS.SCHEDULED)
        self.reservations[reservation.id] = reservation
        return reservation
        
    def getVehicle(self):
        return self.vehicleInventory.getVehicle()

    def cancelReservation(self, reservationId):
        pass

