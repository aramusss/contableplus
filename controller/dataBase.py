__author__ = 'adria'

#!/usr/bin/python

import os.path

class DataBase:
    def __init__(self, rutaUsers="../database/usuaris.txt", rutaComptes="../database/comptes.txt"):
        self.rutaUsers = rutaUsers
        self.rutaComptes = rutaComptes

    #User management methods:
    def creaUsers(self):
        """Creates users file"""
        if self.comprovaUsers():
            print("Users' file already exists!")
        else:
            open(self.rutaUsers, 'w').close()

    def comprovaUsers(self):
        """Comprova que existeixi el fitxer on es guarden els usuaris"""
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
        llista.pop()
        #fer alguna cosa si no troba usuaris?
        return llista

    def afegeixUsuari(self, dni, nombre, apellidos):
        """Afegeix un usuari al fitxer d'usuaris sense comprovar que existeixi"""
        added = False
        if self.comprovaUsers():
            if dni and nombre and apellidos:
                with open(self.rutaUsers, 'a') as f:
                    f.write(dni+","+nombre+","+apellidos+"\n")
                    added = True
            else:
                print("Error, a user can't have empty fields")
        else:
            print("Error! couldn't find users file")
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
                    if linia.split(",")[0] != dni:
                        file.write(linia)
                    else:
                        trobat = True
            if not trobat:
                print("No s'ha trobat l'usuari!")
                #error
        else:
            print("Error! no s'ha trobat el fitxer")

    #Account management methods:
    def creaComptes(self):
        """Creates accounts file"""
        if self.comprovaComptes():
            print("Accounts file already exists!")
        else:
            open(self.rutaComptes, 'w').close()

    def comprovaComptes(self):
        """Checks if the accounts' file (self.rutaComptes) exists"""
        result = False
        if os.path.isfile(self.rutaComptes):
            result = True
        return result

    def llegeixComptes(self):
        """Reads all the accounts' file"""
        resultat = ""
        if self.comprovaComptes():
            with open(self.rutaComptes, 'r') as f:
                resultat = f.read()
        else:
            print("Error! no s'ha trobat el fitxer de comptes")
            #llençar una excepcio
        return resultat

    def llistaComptes(self):
        """Returns a list of all the accounts"""
        list = []
        text = self.llegeixComptes()
        listbylines = text.split("\n")
        for linia in listbylines:
            list.append(linia.split(","))
        if len(list) > 0:
            list.pop()
        return list

    def llistaIBAN(self):
        """Returns a list of all the IBAN codes of the bank accounts"""
        list = []
        accounts = self.llistaComptes()
        for a in accounts:
            list.append(a[0])
        return list

    def afegeixCompta(self, iban, balance, currency, *owners):
        """Adds a new bank account, all filds are mandatory"""
        #comprovar que tots els owners existeixin?
        added = False
        ibanExists = False
        if self.comprovaComptes():
            ibanList = self.llistaIBAN()
            for i in ibanList:
                if i == iban:
                    ibanExists = True
            if not ibanExists:
                if iban and balance and currency and (len(owners) > 0) and ("" not in owners) and (None not in owners):
                    ownerslist = ""
                    for o in owners:
                        ownerslist += o + ","
                    ownerslist = ownerslist[:len(ownerslist)-1]
                    with open(self.rutaComptes, 'a') as f:
                        f.write(iban+","+balance+","+currency+","+"".join(ownerslist)+"\n")
                        added = True
                else:
                    print("Error, a bank account can't have any empty fields")
            else:
                print("Error: bank account could not be added: IBAN code already exists")
        else:
            print("Error: could not find bank accounts' file")
        return added