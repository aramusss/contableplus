import re
import string

class Owner:
    def __init__(self, dni, apellidos, nombre):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni

    def muestraDatos(self):
        return [self.nombre, self.apellidos, self.dni]
    def getDni(self):
        return self.dni

    def validaDNI(self, dni):

        #comprueba la longitud del dni
        if len(dni)<9 or len(dni)>9:
            print('Error: DNI has 9 lenght.')
            return False

        # Convertimos las letras a mayuscula en caso de tener letras en minuscula
        dni = string.upper(dni)

        # Comprobamos que las caracteristicas del NIE se cumplan
        if re.match("[A-Z]", dni[0]):
            if 'X' in dni[0]:
                dni = dni.replace('X','0')
            elif 'Y' in dni[0]:
                dni = dni.replace('Y','1')
            elif 'Z' in dni[0]:
                dni = dni.replace('Z','2')
            else:
                print("Error: Invalid DNI")
                return False

        # Comprobamos que tenemos 8 digitos numericos
        if not re.match("\d{8}", dni[:8]):
            print("Error: DNI need 8 numeric numbers")
            return False

        # Comprobamos que tenemos una letra al final
        if not re.match("[A-Z]", dni[8]):
            print("Error: DNI needs one letter")
            return False

        # Comprobamos si la letra es correcta
        tabla = ("TRWAGMYFPDXBNJZSQVHLCKE")
        if tabla[int(dni[:8]) % 23]==dni[8]:
            print("Correct DNI")
            return True
        else:
            print("Error: Invalid DNI")
            return False


