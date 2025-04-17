#31 Marzo 2025

class Cestino:
    
    def __init__(self,q=None):
        # q èuna lista di frutti da mettere nel cestino, eventualmente vuoti
        self.cestino = set()
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
        c = 0
        for x in self.cestino:
            c+=x.getPeso()
        return c
    

    def len(self):
        return len(self.cestino)
    
    def __str__(self):
        s = ""
        for x in self.cestino:
          s += str(x)
          s += "\n"
        return s