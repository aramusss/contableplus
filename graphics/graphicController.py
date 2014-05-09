__author__ = 'aram'

import turtle
import datetime

#DNI;IBAN;DATE(24/02/2014);+/-IMPORT

class GraphicController:

    def showGrapicWithDNI(self, inputIban):
        filePath = "../database/log.txt"

        actualMoney = 0
        maxMoney = 0
        minMoney = 0
        startDate = datetime.datetime(2014, 1, 1)
        maxDate = startDate

        with open(filePath, 'r') as logDB:
            for line in logDB:
                    dni, iban, date, money = line.split(";")

                    day = int(date[0:2])
                    month = int(date[3:5])
                    year = int(date[6:10])

                    dateTime = datetime.datetime(year, month, day)

                    if(iban == inputIban):
                        if float(money) > maxMoney:
                            maxMoney = float(money) + maxMoney
                        if dateTime > maxDate:
                            maxDate = dateTime
                        if float(money) < minMoney:
                            minMoney = float(money)


        dateDiff = maxDate - startDate

        totalDays = dateDiff.days

        t = turtle.Turtle()

        screen = t.getscreen()

        screen.setworldcoordinates(0, minMoney, totalDays, maxMoney)

        t.goto(minMoney, 0)

        screen.tracer(100)

        t.color("#7D7EC0")
        t.fillcolor("#7D7EC0")
        t.begin_fill()

        file = open("../database/log.txt", "r")

        for line in file:
            dni, iban, date, money = line.split(";")
            actualMoney = actualMoney + float(money)
            day = int(date[0:2])
            month = int(date[3:5])
            year = int(date[6:10])
            if iban == inputIban:
                dateTime = datetime.datetime(year, month, day)
                dateDiff = dateTime - startDate

            t.goto(dateDiff.days, actualMoney)
        t.goto(totalDays, 0)
        t.goto(minMoney, 0)
        t.end_fill()

        screen.update()
        screen.exitonclick()