class Product:
    def __init__(self, name, price, productCode, productType) -> None:
        self.productCode = productCode
        self.name = name
        self.price = price
        self.productType = productType
        self.isSold = False

    def __str__(self) -> str:
        return '{} ({}) : {}'.format(self.name, self.productCode, self.price)