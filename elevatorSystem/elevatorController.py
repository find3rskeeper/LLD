from elevatorTrolley import ElevatorTrolley

class ElevatorController:
    def __init__(self, id, buttons) -> None:
        self.id = id
        self.elevator = ElevatorTrolley(buttons)
    
    def request(self, floor, direction):
        print('Adding request for floor {} and direction {}. Elevator ID {}'.format(floor, direction, self.id))
        self.addRequest(floor, direction)
    

    def addRequest(self, floor, direction):
        pass

    def process(self):
        pass

