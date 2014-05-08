from converter import *
from dataBase import *

converter=converter()
class operations:
    iban=1
    inputString=''
    owner_money=[3456.00,'EUR']
    money_transfered=[200.00,'USD']

    # iban=iban
    # owner_money=[float, currency]
    # owner_curr=currency
    # money_transfered=[money, currency]
    def __init__(self, iban, owner_money,money_transfered):
        self.iban=iban
        self.owner_money=owner_money
        converter.set_localAmount(owner_money)
        self.money_transfered=money_transfered
    def addMoney(self):
        converter.set_amount(self.money_transfered[0])
        boolean=False
        inputString=''
        while(not boolean):
            print('Your local currency is set to '+self.money_transfered[1]+ ' do you want to change it?')
            a=input('Y/N')
            if(a=='Y'):
                inputString=input('input the 3 letters of the currency')
                boolean=converter.set_locale(inputString)
            elif(a=='N'):
                boolean=converter.set_locale(self.money_transfered[1])
            elif(a=='n'):
                boolean=converter.set_locale(self.money_transfered[1])
            elif(a=='y'):
                inputString=input('input the 3 letters of the currency')
                boolean=converter.set_locale(inputString)
            else:
                print("Wrong key")
        self.money_transfered[0]=converter.convert_to_locale(self.money_transfered)
        self.owner_money[0]=converter.convert_to_locale(self.owner_money)
        self.owner_money[1]=converter.get_locale()
        self.owner_money[0]=float(self.money_transfered[0])+float(self.owner_money[0])