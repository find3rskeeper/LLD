from abc import ABC

class State:
    def __init__(self, vendingMachine) -> None:
        self.vendingMachine = vendingMachine

    def pressInsertCoinButton(self):
        raise NotImplementedError('pressInsertCoinButton not implemented')
    
    def insertCoin(self):
        raise NotImplementedError('insertCoin not implemented')

    def pressCancel(self):
        raise NotImplementedError('pressCancel not implemented')

    def pressSelectProductButton(self):
        raise NotImplementedError('pressSelectProductButton not implemented')

    def enterProductCode(self):
        raise NotImplementedError('enterProductCode not implemented')

    def refund(self):
        raise NotImplementedError('refund not implemented')

    def returnChange(self):
        raise NotImplementedError('returnChange not implemented')

    def pressDispatchButton(self):
        raise NotImplementedError('pressDispatchButton not implemented')

    def dispatch(self):
        raise NotImplementedError('dispatch not implemented')
