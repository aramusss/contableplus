import urllib.request
class converter:
    localCurrency='EUR'
    localAmount=0.00
    amount=0.00
    currencies='currencies.txt'
    def set_locale(self,currency):
        boolean=False
        with open(self.currencies, mode='r', encoding='ISO-8859-1') as file:
            for line in file:
                tempCurrency=(line.split(':',1))[0];
                if(currency==tempCurrency):
                    boolean=True
        if(boolean):
            self.localCurrency=currency
        else:
            print("Divisa no valida")
        return boolean
    def convert_to_locale(self,amount):
        boolean=False
        with open(self.currencies, mode='r', encoding='ISO-8859-1') as file:
            for line in file:
                tempCurrency=(line.split(':',1))[0];
                if(amount[1]==tempCurrency):
                    boolean=True
        if boolean:
            url='http://www.google.com/finance/converter?a='+str(amount[0])+'&from='+str(amount[1])+'&to='+str(self.localCurrency)
            response = urllib.request.urlopen(url)
            html = response.read().decode("ISO-8859-1")
            palabras=html.split()
            listaentera="".join(palabras)
            cosaquequiero="<spanclass=bld>"
            cosaquequiero2="</span>"
            print (listaentera)
            numero=(listaentera.find(cosaquequiero))
            numero2=(listaentera.find(cosaquequiero2))
            valor=listaentera[numero+15:numero2-3]
            print (str(amount[0])+" "+str(amount[1])+" son "+valor+" "+str(self.localCurrency))
            return valor
    def convert_from_locale(self,amount):
        boolean=False
        with open(self.currencies, mode='r', encoding='ISO-8859-1') as file:
            for line in file:
                tempCurrency=(line.split(':',1))[0];
                if(amount[1]==tempCurrency):
                    boolean=True
        if boolean:
            url='http://www.google.com/finance/converter?a='+str(amount[0])+'&from='+str(self.localCurrency+'&to='+str(amount[1]))
            response = urllib.request.urlopen(url)
            html = response.read().decode("ISO-8859-1")
            palabras=html.split()
            listaentera="".join(palabras)
            cosaquequiero="<spanclass=bld>"
            cosaquequiero2="</span>"
            print (listaentera)
            numero=(listaentera.find(cosaquequiero))
            numero2=(listaentera.find(cosaquequiero2))
            valor=listaentera[numero+15:numero2-3]
            print (str(amount[0])+" "+str(self.localCurrency)+" son "+valor+" "+str(amount[1]))
            return valor
amount=(120.00,'EUR')
clase2=converter()
clase2.set_locale('USD')
clase2.convert_from_locale(amount)