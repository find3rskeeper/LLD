from seatType import SEATTYPE

class Seat:
    def __init__(self, seatNo, seatType, price) -> None:
        self.seatNo = seatNo
        self.booked = False
        self.type =  seatType if seatType else SEATTYPE.STANDARD
        self.price = price
    
    def book(self):
        self.booked = True
    
    def getPrice(self):
        return self.price

    def isBooked(self):
        return self.booked