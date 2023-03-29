from display import Display
from status import STATUS
from directionEnum import DIRECTION

class ElevatorTrolley:
    def __init__(self, buttons):
        self.display = Display()
        self.currentFloor = 0
        self.direction = None
        self.status = None
        self.buttons = buttons
    
    def pressFloorButton(self, floorNo):
        direction = None
        if floorNo > self.currentFloor:
            direction = DIRECTION.UP
        else:
            direction = DIRECTION.DOWN

        self.buttons[floorNo].press(direction)

    def move(self, floorNo):
        self.status = STATUS.MOVING
        print('Elevator trolley moved to floorNo {}'.format(floorNo))
        self.currentFloor = floorNo
        self.status = STATUS.STOPPED