#Version 1.2.4 21/04/2025<

class Cestino:
    
    def __init__(self,q=None):
        # q èuna lista di frutti da mettere nel cestino, eventualmente vuoti
        self.cestino = set()
        self.tara = 20
        if not q is None:
            for x in q:
                self.add(x)

    def add(self, f):
        self.cestino.add(f)
    
    def costo(self):
        c = 0.0
        for x in self.cestino:
            c+=x.costo()
        return round(c,2)
    
    def netto(self):
        c = self.tara
        for x in self.cestino:
            c+=x.getPeso()
        return c
    
    def getTara(self):
        return str(self.tara)

    def len(self):
        return len(self.cestino)
    
    def __str__(self):
        s = ""
        for x in self.cestino:
          s += str(x)
          s += "\n"
        return s
