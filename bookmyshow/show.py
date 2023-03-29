from seat import Seat
from booking import Booking

class Show:
    def __init__(self, movie, startTime, endTime, screen, price) -> None:
        self.movie = movie
        self.startTime = startTime
        self.endTime = endTime
        self.filledSeats = []
        self.seats = {}
        self.screen = screen
        for seatId in range(screen.seatCount):
            self.seats[seatId] = Seat(seatId, None, price)
    
    def bookSeats(self, seatNos):
        for seat in seatNos:
            if self.seats[seat].isBooked():
                return 'Seat is Booked'

        bookedSeats = []
        total = 0
        for seat in seatNos:
            self.seats[seat].book()
            bookedSeats.append(self.seats[seat])
            total += self.seats[seat].getPrice()
        
        print(self)
        return Booking(1, 1, bookedSeats, total)
            
    def __str__(self):
        seatString = "" 
        for seat in self.seats:
            if self.seats[seat].isBooked():
                seatString += "F "
            else:
                seatString += str(self.seats[seat].seatNo) + " "
        
        return seatString

