from converter import *
from dataBase import *

converter=converter()
owner=1
owner_money=3456
owner_curr='EUR'
receiver_money=1424
receiver_curr='EUR'
boolean=True
print('Your local currency is set to '+owner_curr+ ' do you want to change it?')
a=input('Y/N')
while(boolean):
    if(a.ascii_uppercase=='Y'):
        owner_curr=input('input the 3 letters of the currency')
        owner_money=converter.convert_to_locale(owner_money)
    boolean=converter.set_locale(owner_curr)
converter.set_locale(receiver_curr)
owner_money=converter.convert_to_locale(owner_money)
receiver_money=owner_money+receiver_money