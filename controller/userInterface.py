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
        #select one iban, that we will be working on.
        currentIbanOption =input("Select one IBAN:")
        currentIban = ibanList[int(currentIbanOption)-1]
        #if currentIban is correct, should display options to do:
        print("1: Show Graphics from this account")
        #Show graphics
        print("2: Add or Withdraw money")
        #Add or withdraw money
        print("3: Add another Owner")
        #Add another owner(?)
        option = input("Select an option: ")

        if(option == "1"):
            myTest = GraphicController()
            myTest.showGrapicWithDNI(currentIban)
        if(option == "2"):
            money_input=input("how much money will you put?")
            curr_input=input("and what currency is it?")
            new_money=[float(money_input),curr_input]
            currentOwner = currentUser.getOwner()
            currentDni = currentOwner.getDni()
            operations= Operations(currentIban, new_money, currentDni)
        if(option == "3"):
            # I BET U CAN'T...
            print("other thing..")
    else:
        print("Would you like to create one?")
        createOne = input("Y/N: ")
        if createOne == "Y":
            print("Lets create an account.")
            registerAcc = DataBase()
            currency = "EUR"
            amount = input("Insert your diposit: ")
            owner = currentUser.getOwner()
            dni = owner.getDni()
            print(dni)
            #this creates a new account.
            registerAcc.afegeixCompta(amount, currency, dni)

else:
    pass