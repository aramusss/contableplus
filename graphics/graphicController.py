__author__ = 'aram'

from graphics import *

#DNI;IBAN;DATE(24/02/2014);+/-IMPORT

class GraphicController:
    def showGrapicWithDNI(self, inputDni):
        win =  GraphWin
        filePath = ""
        with open(filePath, 'r') as logDB:
            for line in logDB:
                    dni, iban, date, money = line.split(";")
                    if(dni == inputDni):
