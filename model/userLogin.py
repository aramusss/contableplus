__author__ = 'adria'

#!/usr/bin/python

import dataBase #no mel agafa...
#import owner el fitxer "owner" no es un .py i per tant encara no es pot importar...

class UserLogin:
    def __init__(self, dni, nom):
        self.dni = dni
        self.nom = nom
        self.db = dataBase()


    def login(self):
        """Comproba que l'usuari (nom i dni) esigui en la bbdd i autentifica l'usuari"""
        pass

    def llistaUsuaris(self):
        """Llista tots els usuaris registrats"""
        pass

    def existeixUsuari(self):
        """Comprova que existeixi l'usuari actual (self.usuari)"""
        pass

    def guardaUsuari(self, owner):
        """Guarda en el fitxer l'usuari actual (self.usuari)"""
        pass
