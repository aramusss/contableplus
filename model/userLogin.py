__author__ = 'adria'

#!/usr/bin/python

from owner import *
from dataBase import *

class UserLogin:
    def __init__(self, owner):
        self.owner = owner
        self.db = dataBase()


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

    def existeixUsuari(self, usuari = self.owner.dni):
        """Checks if a user exists by searching the DNI in the database"""
        exists = False
        for dni in self.llistaDNI():
            if dni == usuari:
                exists = True
        return exists

    def guardaUsuari(self, owner):
        """Guarda en el fitxer l'usuari actual (self.usuari)"""
        pass
