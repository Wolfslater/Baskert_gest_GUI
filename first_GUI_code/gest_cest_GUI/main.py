#31 Marzo 2025


from Frutto import *
from Cestino import *

def inputfrutto():
    nome=input("inserisci il nome del frutto : \n")
    prezzo=float(input("inserisci il prezzo del frutto : \n"))
    peso=int(input("inserisci il peso del frutto : \n"))
    frutto=Frutto([nome,prezzo,peso])
    return frutto

if __name__ == '__main__':
    print("creo cestino \n ")
    cest = Cestino()
    a=0
    while a<6:
        print("[0] aggiungi Frutto")
        print("[1] aggiungi Frutto a caso ")
        print("[2] stampa peso netto del cestino ")
        print("[3] stampa costo totale del cestino ")
        print("[4] stampa cestino")
        print("[5] to print tara ")
        print("[6] esci")
        a=int(input("inserisci l'opzione: "))
        if a==0:
            cest.add(inputfrutto())
            
        elif a==1:
            cest.add(Frutto())
            
        elif a==2:
            if cest.netto()==0:
                print("non ci sono frutti nel cestino")
            else:
                print("il peso netto del cestino è: ",cest.netto(),"gr")

        elif a==3:
            if cest.costo()==0:
                print("non ci sono frutti nel cestino")
            else:
                print("il costo totale del cestino è", cest.costo(),"€")
        elif a == 4:
            if cest.len()==0:
                print("non ci sono frutti nel cestino")
            else:
                print(cest)
        elif a == 5:
            print(cest.getTara())