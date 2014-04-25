
class Account:
    def __init__(self, iban, titular, moneda):
        self.iban = iban
        self.titular = titular
        self.moneda = moneda

    def muestraDatos(self):
        return [self.iban, self.titular, self.moneda]

    @property
    def iban(self):
        return self.iban

    @iban.setter
    def iban(self, value):
        self.iban = value


    @property
    def titular(self):
        return self.titular

    @titular.setter
    def titular(self, value):
        self.titular = value


    @property
    def moneda(self):
        return self.moneda

    @moneda.setter
    def moneda(self, value):
        self.moneda = value


