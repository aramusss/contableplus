__author__ = 'aram'

from userLogin import *

#This class will be the one that controls
#the inputs and outputs for the user interface.

print("Hello Worker! Welcome to ContablePlus!")
currentUser = UserLogin(None)
currentUser.enterLogin()
if(currentUser.registered):
    print("What do you want to do?")
    #list ibans
    print("List of available accounts:")
    ibanList = currentUser.getIbanList()
    for iban in ibanList:
        print(iban)
    #select one iban

else:
    pass