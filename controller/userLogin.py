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


    def login(self, owner=None):
        """Checks if the user is on the database and logs in"""
        if owner is not None:
            self.owner = owner
        if self.userExists():
            if self.checkUser():
                self.registered = True
                print("You have succesfully logged in")
            else:
                print("Error! name or surname incorrect")
        else:
            print("Error, user with DNI "+owner.dni+" doesn't exist")

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
        """Checks if user self.owner is on the database"""
        result = False
        for user in self.db.llistaUsers():
            if user.dni == self.owner.dni:
                if user.nombre == self.owner.nombre and user.nombre == self.owner.nombre:
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
            print("User "+owner.dni+" already exists!")
        else:
            result = self.db.afegeixUsuari(owner.dni, owner.nombre, owner.apellidos)
            if result:
                print("Usuar added!")
            else:
                print("User could not be added")