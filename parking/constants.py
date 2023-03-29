from ParkingVehicleType import ParkingVehicleType
from compactParkingSpot import CompactParkingSpot
from smallParkingSpot import SmallParkingSpot
from largeParkingSpot import LargeParkingSpot
from parkingSpotType import ParkingSpotType
from vehicleCleaning import VehicleCleaning

VehicleSpotMapping = {
            ParkingVehicleType.MotorCycle.name: (ParkingSpotType.COMPACT ,CompactParkingSpot),
            ParkingVehicleType.Car.name: (ParkingSpotType.SMALL, SmallParkingSpot),
            ParkingVehicleType.SUV.name: (ParkingSpotType.SMALL, SmallParkingSpot),
            ParkingVehicleType.Truck.name: (ParkingSpotType.LARGE, LargeParkingSpot),
}

ParkingSpotMapping = {
    ParkingSpotType.COMPACT.name.lower(): CompactParkingSpot,
    ParkingSpotType.SMALL.name.lower(): SmallParkingSpot,
    ParkingSpotType.LARGE.name.lower(): LargeParkingSpot
}

addOnServices = [
    VehicleCleaning
]