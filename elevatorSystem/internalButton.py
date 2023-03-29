from button import Button

class InternalButton(Button):
    def __init__(self, floorNo) -> None:
        super().__init__()
        self.floorNo = floorNo
    
    def addIBDispatcher(self, ibDispatcher):
        self.ibDispatcher = ibDispatcher

    def press(self, direction):
        print('Button with Floor No {} pressed for direction {}'.format(self.floorNo, direction))
        self.ibDispatcher.dispatch(self.floorNo, direction)
