class Reservation:
    def __init__(self, reservationId, vehicle, person, pickupTime, dropTime, pickupLocation, dropLocation, rvStatus):
        self.id = reservationId, 
        self.vehicle = vehicle
        self.person = person
        self.pickupTime = pickupTime
        self.dropTime = dropTime
        self.pickupLocation = pickupLocation
        self.dropLocation = dropLocation
        self.status = rvStatus
    
    def complete(self):
        pass
    
    def cancel(self):
        pass