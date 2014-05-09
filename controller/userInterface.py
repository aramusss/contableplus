__author__ = 'aram'

from userLogin import *
from dataBase import *
import os.path, random

#This class will be the one that controls
#the inputs and outputs for the user interface.

print("Hello Worker! Welcome to ContablePlus!")
currentUser = UserLogin(None)
currentUser.enterLogin()
if(currentUser.registered):
    print("What do you want to do?")
    #if it have ibans select an account
    ibanList = currentUser.getIbanList()
    if ibanList:
        #list ibans
        print("List of available accounts:")
        for iban in ibanList:
            print(iban)
        #select one iban
            input("Select one IBAN:")

    else:
        print("Would you like to create one?")
        createOne = input("Y/N: ")
        if createOne == "Y":
            print("Lets create an account.")
            registerAcc = DataBase()
            amount = input("Insert your diposit: ")
            currency = "EUR"
            owner = currentUser.getOwner()
            dni = owner.getDni()
            print(dni)
            registerAcc.afegeixCompta(amount, currency, dni)


else:
    pass