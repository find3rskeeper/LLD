from button import Button

class ExternalButton(Button):
    def __init__(self, floorNo, direction, EBDispatcher) -> None:
        super().__init__()
        self.floorNo = floorNo
        self.direction = direction
        self.EBDispatcher = EBDispatcher
    
    def press(self):
        print('Elevator is called on {} Floor to go {}'.format(self.floorNo, self.direction))
        self.EBDispatcher.dispatch(self.floorNo, self.direction)