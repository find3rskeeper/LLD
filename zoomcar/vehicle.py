from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self, vehicleId, vehicleNo, wheels) -> None:
        self.vehicleId = vehicleId
        self.vehicleNo = vehicleNo
        self.status = None
        self.color = None
        self.make = None
        self.model = None
        self.wheels = wheels
        self.kmDriven = None

    
    def updateStatus(self, status):
        self.status = status

