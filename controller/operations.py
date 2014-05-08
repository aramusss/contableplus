from converter import *
from dataBase import *

converter=converter()
owner=1
inputString=''
owner_money=3456
converter.set_localAmount(3456)
money_transfered=[200,'EUR']
receiver_money=1200
receiver_curr='EUR'
if(owner_money>=money_transfered[0]):
    converter.set_amount(money_transfered[0])
    boolean=False
    while(not boolean):
        print('Your local currency is set to '+money_transfered[1]+ ' do you want to change it?')
        a=input('Y/N')
        if(a=='Y'):
            inputString=input('input the 3 letters of the currency')
            money_transfered[1]=inputString
            boolean=converter.set_locale(money_transfered[1])
        elif(a=='N'):
            boolean=True
        elif(a=='n'):
            boolean=True
        elif(a=='y'):
            inputString=input('input the 3 letters of the currency')
            money_transfered[1]=inputString
            boolean=converter.set_locale(money_transfered[1])
        else:
            print("Wrong key")
    money_transfered[0]=converter.convert_to_locale(money_transfered)
    converter.set_locale(receiver_curr)
    money_transfered[0]=converter.convert_to_locale(money_transfered)
    receiver_money=money_transfered[0]+receiver_money
print(receiver_money)