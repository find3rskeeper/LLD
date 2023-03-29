class Payment:
    def __init__(self, amount, isPaid = None) -> None:
        self.amount = amount
        self.isPaid = isPaid if isPaid == True else False
    
    def complete(self):
        self.isPaid = True
    
    def isComplete(self):
        return self.isPaid