class InternalButtonDispatcher:
    def __init__(self, elevatorController) -> None:
        self.EVController = elevatorController
        pass

    def dispatch(self, floorNo, direction):
        self.EVController.request(floorNo, direction)
