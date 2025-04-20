#31 Marzo 2025

import random

class Frutto:
    def __init__(self, q=["", "", ""]):
        if q == ["", "", ""]:
            x = random.randint(0,1)
            if x==0:
                self.nome = "Ciliegia"
                self.prezzo_kg = round(random.uniform(5,9),2)
                self.peso_gr = random.randint(2,25)
            else:
                self.nome = "Pesca"
                self.prezzo_kg = round(random.uniform(2,7),2)
                self.peso_gr = random.randint(15,60)
        else:
            self.nome = q[0]
            self.prezzo_kg = float(q[1])
            self.peso_gr = int(q[2])

    def __str__(self):
        s = ""
        s += self.nome + " ("
        s += "peso " + str(self.peso_gr) + " gr, "
        s += "prezzo " + str(self.prezzo_kg) + " €/kg"
        s += ", costo " + str(self.costo()) + " €)"
        return s

    def getNome(self):
        return self.nome
    def getPrezzo(self):
        return self.prezzo_kg
    def getPeso(self):
        return self.peso_gr
    
    def setNome(self, x):
        self.nome = x
    def setPrezzo(self, x):
        self.prezzo_kg = x
    def setPeso(self, x):
        self.peso_gr = x
    
    def costo(self):
        c  = (self.peso_gr / 1000) * self.prezzo_kg
        return round(c,2)
    
