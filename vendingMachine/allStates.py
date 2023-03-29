from state import State

class IdleState(State):
    def __init__(self, vendingMachine) -> None:
        super().__init__(vendingMachine)

    def pressInsertCoinButton(self):
        print('Insert Coin Button Pushed')
        self.vendingMachine.setState(AddCoinState(self.vendingMachine))
    
    def pressCancel(self):
        print('Cancelled Pressed')


class AddCoinState(State):
    def __init__(self, vendingMachine) -> None:
        super().__init__(vendingMachine)
    
    def addCoin(self, coin):
        self.vendingMachine.addCoin(coin)
        print('Coin Accepted')
    
    def pressCancel(self):
        total = self.vendingMachine.refund()
        print('Cancel pressed in add coin state')
        self.vendingMachine.setState(IdleState(self.vendingMachine))
        return total
        
    def pressSelectProductButton(self):
        print('Select Product Button Pressed')
        self.vendingMachine.setState(SelectProductState(self.vendingMachine))


class SelectProductState(State):
    def __init__(self, vendingMachine) -> None:
        super().__init__(vendingMachine)
    
    def enterProductCode(self, productCode):
        print('Product Code Entered {}'.format(productCode))
        self.vendingMachine.addProductCode(productCode)
    
    def pressDispatchButton(self):
        print('Dispatch button pressed')
        try:
            self.vendingMachine.dispatch()
            self.vendingMachine.returnChange()
        
        except Exception as e:
            print('Cannot dispense product', e)
            self.vendingMachine.refund()
            # raise e

        self.vendingMachine.setState(IdleState(self.vendingMachine))
    
    def pressCancel(self):
        self.vendingMachine.refund()
        self.vendingMachine.setState(IdleState(self.vendingMachine))


# class DispatchState(State):
#     def __init__(self, vendingMachine) -> None:
#         super().__init__(vendingMachine)
#         self.dispatch()
    
#     def pressCancel(self):
#         total = self.vendingMachine.refund()
#         self.vendingMachine.setState(IdleState(self.vendingMachine))
#         return total

#     def dispatch(self):
#         print('Product Dispatched')
#         self.vendingMachine.setState(IdleState(self.vendingMachine))