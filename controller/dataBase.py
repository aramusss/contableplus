__author__ = 'adria'

#!/usr/bin/python

import os.path

class DataBase:
    def __init__(self, rutaUsers="../database/usuaris.txt", rutaComptes="../database/comptes.txt"):
        self.rutaUsers = rutaUsers
        self.rutaComptes = rutaComptes

    def creaUsers(self):
        """Creates users file"""
        if self.comprovaUsers():
            print("Users' file already exists!")
        else:
            open(self.rutaUsers, 'w').close()

    def creaComptes(self):
        """Creates accounts file"""
        if self.comprovaComptes():
            print("Accounts file already exists!")
        else:
            open(self.rutaComptes, 'w').close()

    def comprovaUsers(self):
        """Comprova que existeixi el fitxer on es guarden els usuaris"""
        result = False
        if os.path.isfile(self.rutaUsers):
            result = True
        return result

    def comprovaComptes(self):
        """Comprova que existeixi el fitxer on es guarden les comptes bancaries"""
        result = False
        if os.path.isfile(self.rutaComptes):
            result = True
        return result

    def llegeixUsers(self):
        """Llegeix tot el fitxer d'usuaris, els retorna en una string"""
        resultat = ""
        if self.comprovaUsers():
            with open(self.rutaUsers, 'r') as f:
                resultat = f.read()
        else:
            print("Error! no s'ha trobat el fitxer d'usuaris")
            #llençar una excepcio
        return resultat

    def llistaUsers(self):
        """Agafa els usuaris (amb el seu dni, nom i cognoms) i els retorna en una llista"""
        llista = []
        text = self.llegeixUsers()
        llistacomes = text.split("\n")
        for linia in llistacomes:
            llista.append(linia.split(","))
        llista.pop()
        #fer alguna cosa si no troba usuaris?
        return llista

    def llegeixComptes(self):
        """Llegeix tot el fitxer de comptes"""
        resultat = ""
        if self.comprovaComptes():
            with open(self.rutaComptes, 'r') as f:
                resultat = f.read()
        else:
            print("Error! no s'ha trobat el fitxer de comptes")
            #llençar una excepcio
        return resultat

    def afegeixUsuari(self, dni, nombre, apellidos):
        """Afegeix un usuari al fitxer d'usuaris sense comprovar que existeixi"""
        added = False
        if self.comprovaUsers():
            with open(self.rutaUsers, 'a') as f:
                f.write(dni+","+nombre+","+apellidos+"\n")
                added = True
        else:
            print("Error! no s'ha trobat el fitxer d'usuaris")
        return added

    def esborraUsuari(self, dni):
        """Esborra un usuari al fitxer d'usuaris sense comprovar que existeixi"""
        if self.comprovaUsers():
            file = open(self.rutaUsers, 'r')
            llista = file.readlines()
            file.close()
            trobat = False
            with open(self.rutaUsers, 'w') as file:
                for linia in llista:
                    print(linia.split(",")[0])
                    print("---")
                    if linia.split(",")[0] != dni:
                        file.write(linia)
                    else:
                        trobat = True
            if (not trobat):
                print("No s'ha trobat l'usuari!")
                #error
        else:
            print("Error! no s'ha trobat el fitxer")