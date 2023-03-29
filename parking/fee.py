
class Fee:
    def __init__(self, duration, charge, rateType = 'flatRate', nextFee = None):
        self.duration = duration
        self.charge = charge
        self.nextFee = nextFee
        self.rateType = rateType
    
    def setNextFee(self, nextFee):
        self.nextFee = nextFee
        return

    def calculateFee(self, duration):
        currentFee = 0
        if self.duration > duration:
            remainingDuration = 0
        else:
            remainingDuration  = duration - self.duration + 1
            duration = self.duration - 1

        currentFee = duration * self.charge if self.rateType == 'perHour' else self.charge

        if not self.nextFee or remainingDuration <= 0:
            return currentFee
        
        return currentFee + self.nextFee.calculateFee(remainingDuration)
