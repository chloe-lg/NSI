import os

class Noeud:
    def __init__(self, v, f):
        self.valeur = v
        self.fils = f

    
a = Noeud("A", [Noeud("B", [Noeud("D", [])]), 
                Noeud("C", [
                            Noeud("E", []),
                            Noeud("F", [Noeud("H", [])]), 
                            Noeud("G", []), 
                            ])
                ])

def affiche(a, marge = ""):
    print(marge + a.valeur)
    for f in a.fils:
        affiche(f, marge + " ")


def repertoire(r):
    b = Noeud(r, [])
    if os.path.isdir(r) == True:
        t = os.listdir(r)
        for elt in t:
          ab = os.path.join(r, elt)
          b.fils.append(repertoire(ab))
    return b
    

        

x = repertoire("/Document/NSI/exercice")
h = 1
