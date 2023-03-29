
class VendingMachine:
    def __init__(self, state, total) -> None:
        self.state = state
        self.coins = []
        self.total = total
        self.catalog = {}

    def addCatalog(self, catalog):
        for product in catalog:
            self.catalog[product.productCode] = product
    
    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def addCoin(self, coin):
        self.coins.append(coin)
    
    def refund(self):
        total = sum(self.coins)
        print('Refunding Amount {}'.format(total))
        self.coins = []

        return total
    
    def addProductCode(self, productCode):
        self.productCode = productCode

    def getProductPrice(self):
        return self.productCatalog[self.productCode].price

    def returnChange(self):
        change = sum(self.coins) - self.catalog[self.productCode].price
        self.total = sum(self.coins) - change
        print('Returning Change {}'.format(change))
        return change

    def dispatch(self):
        product = self.catalog[self.productCode]
        if product.price > sum(self.coins):
            raise Exception('Amount is less')

        print('Dispatching product ' + str(product))

    def __str__(self) -> str:
        returnStr = ''
        for product in self.catalog:
            returnStr += str(self.catalog[product]) + '\n'
        
        return returnStr
        