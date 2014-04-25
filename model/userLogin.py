__author__ = 'adria'

#!/usr/bin/python

from owner import *
from dataBase import *

class UserLogin:
    def __init__(self, owner):
        self.owner = owner
        self.db = DataBase()


    def login(self):
        """Checks if the user is on the database logs in"""
        pass

    def llistaDNI(self):
        """Lists all DNI's"""
        llista = []
        llistacompleta = self.db.llistaUsers()
        for user in llistacompleta:
            llista.append(user[0])
        return llista

    def existeixUsuari(self, dni = None):
        """Checks if a user exists by searching the DNI in the database"""
        if dni == None:
            dni = self.owner.dni
        exists = False
        for dniactual in self.llistaDNI():
            if dniactual == dni:
                exists = True
        return exists

    def guardaUsuari(self, owner=None):
        """Saves owner to the database if it doesn't exist"""
        if owner == None:
            owner = self.owner
        if self.existeixUsuari(owner.dni):
            print("User "+owner.dni+" already exists!")
        else:
            self.db.afegeixUsuari(owner.dni, owner.nombre, owner.apellidos)
            print("Usuari afegit!")