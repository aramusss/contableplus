__author__ = 'aram'

import turtle
import datetime

#DNI;IBAN;DATE(24/02/2014);+/-IMPORT

class GraphicController:

    def showGrapicWithDNI(self, inputDni):
        filePath = "../database/log.txt"

        maxMoney = 0
        startDate = datetime.datetime(2014, 1, 1)
        maxDate = startDate

        with open(filePath, 'r') as logDB:
            for line in logDB:
                    dni, iban, date, money = line.split(";")

                    day = int(date[0:2])
                    month = int(date[3:5])
                    year = int(date[6:10])

                    dateTime = datetime.datetime(year, month, day)

                    #if(dni == inputDni):

                    if int(money) > maxMoney:
                        maxMoney = int(money)
                    if dateTime > maxDate:
                        maxDate = dateTime

        dateDiff = maxDate - startDate

        totalDays = dateDiff.days

        t = turtle.Turtle()

        screen = t.getscreen()

        screen.setworldcoordinates(0,0,totalDays, maxMoney)

        t.goto(0,0)

        screen.tracer(100)

        file = open("../database/log.txt", "r")

        for line in file:
            dni, iban, date, money = line.split(";")

            day = int(date[0:2])
            month = int(date[3:5])
            year = int(date[6:10])

            dateTime = datetime.datetime(year, month, day)

            dateDiff = dateTime - startDate

            t.goto(dateDiff.days, int(money))
        screen.update()
        screen.exitonclick()

myTest = GraphicController()
myTest.showGrapicWithDNI("11111111A")