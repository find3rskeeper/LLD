from externalButton import ExternalButton
from directionEnum import DIRECTION

class Floor:
    def __init__(self, no, EBDispatcher) -> None:
        self.floorNo = no
        self.upButton = ExternalButton(self.floorNo, DIRECTION.UP, EBDispatcher)
        self.downButton = ExternalButton(self.floorNo, DIRECTION.DOWN, EBDispatcher)