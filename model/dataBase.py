__author__ = 'adria'

#!/usr/bin/python

import os.path
#import owner.py el fitxer "owner" no es un .py i per tant encara no es pot importar...

class dataBase:
    def __init__(self, rutaUsers="usuaris.txt", rutaComptes="comptes.txt"):
        self.rutaUsers = rutaUsers
        self.rutaComptes = rutaComptes

    def comprovaUsers(self):
        """Comprova que existeixi el fitxer on es guarden els usuaris"""
        result = False
        if os.path.isfile(self.rutaUsers):
            result = True
        return result

    def comprovaComptes(self):
        """Comprova que existeixi el fitxer on es guarden les comptes bancaries"""
        result = False
        if os.path.isfile(self.rutaUsers):
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

    def afegeixUsuari(self, owner):
        """Afegeix un usuari al fitxer d'usuaris sense comprovar que existeixi"""
        if self.comprovaUsers():
            with open(self.rutaUsers, 'w') as f:    #machaca tot el fitxer...
                f.write(owner.dni+","+owner.nombre+","+owner.apellidos)
        else:
            print("Error! no s'ha trobat el fitxer d'usuaris")

    def esborraUsuari(self, owner):
        """Esborra un usuari al fitxer d'usuaris sense comprovar que existeixi"""
        if self.comprovaUsers():
            llista = self.llistaUsers()
            n = 0
            trobat = False
            for linia in llista:
                if linia[0] == owner.dni:
                    llista.pop(n)
                    trobat = True
                    break
                n = n+1
            if (not trobat):
                print("No s'ha trobat l'usuari!")
                #error
        else:
            print("Error! no s'ha trobat el fitxer d'usuaris")