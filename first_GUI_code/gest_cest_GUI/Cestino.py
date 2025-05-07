#Version 1.2.7 27/04/2025

from random import randint as rnd

class Cestino:
    def __init__(self,q=None):
        # q èuna lista di frutti da mettere nel cestino, eventualmente vuoti
        self.cestino = set()
        self.tare = rnd(1, 50)
        if not q is None:
            for x in q:
                self.add(x)

    def add(self, f):
        self.cestino.add(f)
    
    def getPrice(self):
        c = 0.0
        for x in self.cestino:
            c+=x.price()
        return round(c,2)
    
    def net(self):
        c = 0.0
        for x in self.cestino:
            c+=x.getWeight()
        return c
    
    def grossWeight(self):
        grossWeight = self.getTare()
        if self.net() != 0.0:
            grossWeight = int(self.getTare()) + int(self.getNet())
        return grossWeight
        
    def getTare(self):
        return str(self.tare)

    def len(self):
        return len(self.cestino)
    
    def __str__(self):
        s = ""
        for x in self.cestino:
          s += str(x)
          s += "\n"
        return s
