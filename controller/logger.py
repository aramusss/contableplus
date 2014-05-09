import os.path


class Log:
    def __init__(self, dni, iban, data, saldo):
        self.dni = dni
        self.iban = iban
        self.data = data
        self.saldo = saldo

    def muestraDatos(self):
        return [self.dni, self.iban, self.data, self.saldo]


class Logger:
    #funcion file
    def __init__(self):
        self.file = "../database/log.txt"


    def comprovaLog(self):
        """Comprova que existeixi el fitxer on es guarden els logs"""
        result = False
        if os.path.isfile(self.file):
            result = True
        return result

    def muestraLog(self, dni):
        with open(self.file, mode='r', encoding='UTF-8') as files:
            try:
                for line in files:
                    if (line.split(";")[0] == dni):
                        print(line)
            finally:
                files.close()


#controlar que se introduzca un iban
    def addLog(self, dni, iban, data, saldo):
        if self.comprovaLog():
            with open(self.file, mode='a', encoding='UTF-8') as f:
                f.write(dni+";"+iban+";"+data+";"+saldo+"\n")

        else:
            print("Error, dni can't have empty fields")
        #return added

#
# entrada = 0
# print("Introduce una opción de Menú:")
# print("1-Muestra log por dni:")
# print("2-Añade un log:")
#
#
# entrada = int(input("Introduce un número del menú:"))
#
# while (entrada <= 2):
#     #programa 1
#     if (entrada == 1):
#         #1 muestra
#         func1 = Logger()
#         func1.muestraLog("22222222B")
#         break
#
#     if (entrada == 2):
#         #2 añade
#        # func2 = Log("14270390V", "05/10/2010", "4213412341", "321231")
#         func1 = Logger()
#         func1.addLog("14270390V", "05/10/2010", "4213412341", "321231")
#         break