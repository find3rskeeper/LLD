from paymentStatus import PAYMENT

class Payment:
    def __init__(self, bill, status) -> None:
        self.bill = bill
        self.status = status
    
    def makePayment(self):
        self.status = PAYMENT.PAID
        return