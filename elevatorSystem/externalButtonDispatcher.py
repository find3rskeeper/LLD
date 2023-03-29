class ExternalButtonDispatcher:
    def __init__(self, elevatorControllers) -> None:
        self.elevatorControllers = elevatorControllers

    def dispatch(self, floorNo, direction):
        print('Request came for {}, {}'.format(floorNo, direction))
        evController = self.findController(floorNo, direction)
        evController.request(floorNo, direction)
    
    def findController(self, floorNo, direction):
        return self.elevatorControllers[0]