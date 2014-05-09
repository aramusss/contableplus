__author__ = 'adria'

#!/usr/bin/python

from dataBase import *
import sys
sys.path.insert(0, '../model') #sino no deixa importar...
from owner import *

class UserLogin:
    def __init__(self, owner):
        self.owner = owner
        self.db = DataBase()
        self.registered = False #si l'usuari ja ha fet loguin o no
    def enterLogin(self):
        """Like the 'login' method, but asks for the user data to be written in the terminal"""
        self.askUserData()
        while True:
            result = self.login()
            if result == 1:
                self.askUserData()
            elif result == 2:
                create = input("Would you like to create it?(Y/N): ")
                if create.lower() == "y" or create.lower() == "":
                    self.db.afegeixUsuari(self.owner.dni, self.owner.nombre, self.owner.apellidos)
                break
            else:
                break

    def askUserData(self):
        """Sets the self.owner information with the parameters the user writes on the terminal"""
        while True:
            print("Insert your personal information to log in:")
            name = input("Name: ")
            surname = input("Surname: ")
            dni = input("DNI: ")
            if name and surname and dni:
                self.owner = Owner(dni, surname, name)
                break
            else:
                print("Error, one or more of the fields is empty, write it again:\n")

    def login(self, owner=None):
        """Checks if the user is on the database and logs in"""
        result = 0
        if owner is not None:
            self.owner = owner
        if self.userExists():
            if self.checkUser():
                self.registered = True
                print("You have succesfully logged in\n")
            else:
                print("Error! name or surname incorrect\n")
                result = 1
        else:
            print("Error, user with DNI "+self.owner.dni+" doesn't exist\n")
            result = 2
        return result

    def llistaDNI(self):
        """Lists all DNI's"""
        llista = []
        llistacompleta = self.db.llistaUsers()
        for user in llistacompleta:
            llista.append(user[0])
        return llista

    def userExists(self, dni = None):
        """Checks if a user exists by searching the DNI in the database"""
        if dni is None:
            dni = self.owner.dni
        exists = False
        for dniactual in self.llistaDNI():
            if dniactual == dni:
                exists = True
        return exists

    def checkUser(self):
        """Checks if self.owner data is correct"""
        result = False
        for user in self.db.llistaUsers():
            dni = user[0]
            name = user[1]
            surname = user[2]
            if dni == self.owner.dni:
                if name == self.owner.nombre and surname == self.owner.apellidos:
                    result = True
                break
        return result

    def isLogged(self):
        """Returns if the user is logged in or not"""
        return self.registered

    def guardaUsuari(self, owner=None):
        """Saves owner to the database if it doesn't exist"""
        if owner is None:
            owner = self.owner
        if self.userExists(owner.dni):
            print("User with DNI '"+owner.dni+"' already exists!")
        else:
            result = self.db.afegeixUsuari(owner.dni, owner.nombre, owner.apellidos)
            if result:
                print("User "+owner.nombre+" added!")
            else:
                print("User could not be added")

    def getIbanList(self):
        """Returns a list of the IBAN codes of the owners' accounts"""
        llista = self.db.llistaComptes()
        ibanList = []
        for account in llista:
            for user in account[3:]:
                if user == self.owner.dni:
                    ibanList.append(account[0])
                    break
        return ibanList

    def getOwner(self):
        return self.owner