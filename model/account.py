
class Account:
    def __init__(self, iban, titular, moneda):
        self.iban = iban
        self.titular = titular
        self.moneda = moneda

    def muestraDatos(self):
        return [self.iban, self.titular, self.moneda]

