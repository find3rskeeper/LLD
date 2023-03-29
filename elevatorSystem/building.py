from floor import Floor
from externalButtonDispatcher import ExternalButtonDispatcher
from elevatorController import ElevatorController
from internalButtonDispatcher import InternalButtonDispatcher
from internalButton import InternalButton

class Building:
    def __init__(self, floorCount, elevatorCount) -> None:
        self.floors = []
        self.elevatorControllers = []
        self.IBDispatcher = []
        self.EBDispatcher = None
        
        self.createElevators(floorCount, elevatorCount)
        
        for floorNo in range(floorCount):
            self.floors.append(Floor(floorNo, self.EBDispatcher))
        
        
    
    def createElevators(self, floorCount, elevatorCount):
        #creating elevators
        for elevatorId in range(elevatorCount):

            buttons = []
            #Creating internal elevator buttons
            for floorNo in range(floorCount):
                buttons.append(InternalButton(floorNo))

            elevatorController = ElevatorController(elevatorId, buttons)
            self.elevatorControllers.append(elevatorController)
            IBDispatcher = InternalButtonDispatcher(elevatorController)
            self.IBDispatcher.append(IBDispatcher)

            #Adding internal Dispatcher to internal elevator buttons
            for button in buttons:
                button.addIBDispatcher(IBDispatcher)
            
            
        self.EBDispatcher = ExternalButtonDispatcher(self.elevatorControllers)