from converter import *
from dataBase import *
from logger import *


class Operations:
    dataBase=DataBase()
    converter=Converter()
    iban=1
    inputString=''
    money_transfered=[200.00,'USD']
    dni = ''

    # iban=iban
    # money_transfered=[money, currency]
    def __init__(self, iban,money_transfered, dni):
        self.iban=iban
        self.money_transfered=money_transfered
        self.dni = dni
    #returns a list with the money and the currency
    def addMoney(self):
        self.converter.set_amount(self.money_transfered[0])
        boolean=False
        true_owner_curr='EUR'
        inputString=''
        while(not boolean):
            print('The currency is set to '+self.money_transfered[1]+ ' do you want to change it?')
            a=input('Y/N')
            if(a=='Y'):
                inputString=input('input the 3 letters of the currency')
                boolean=self.converter.set_locale(inputString)
            elif(a=='N'):
                boolean=self.converter.set_locale(self.money_transfered[1])
            elif(a=='n'):
                boolean=self.converter.set_locale(self.money_transfered[1])
            elif(a=='y'):
                inputString=input('input the 3 letters of the currency')
                boolean=self.converter.set_locale(inputString)
            else:
                print("Wrong key")
        self.money_transfered[0]=self.converter.convert_to_locale(self.money_transfered)
        self.converter.set_locale('EUR')
        self.money_transfered[0]=float(self.converter.convert_to_locale(self.money_transfered))
        self.dataBase.modificaCompta(self.iban, float(self.money_transfered[0]))
        log = Log(self.dni, self.iban, self.money_transfered[0])
        log.addLog()
        print('operation succeded')
