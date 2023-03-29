from datetime import datetime
from payment import Payment

class Booking:
    def __init__(self, bookingId, showId, seats, amount) -> None:
        self.seats = seats
        self.bookingId = bookingId
        self.payment = Payment(amount)
        self.showId = showId
        self.amount = amount
        self.date = datetime.now()
    
    def isPaymentComplete(self):
        return self.payment.isComplete()
    
    def makePayment(self):
        return self.payment.complete()