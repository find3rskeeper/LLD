class VehicleInventory:
    def __init__(self, vehicles, freeVehicles) -> None:
        self.vehicles = vehicles
        self.freeVehicles = freeVehicles
    
    def addVehicle(self):
        pass

    def getVehicle(self):
        return self.freeVehicles[0]
    
    def markVehicleReserved(self, vehicleId):
        pass
    
    def markVehicleInactive(self):
        pass