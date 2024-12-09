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

def affiche(a, marge = "")
   print(marge + a.valeur)
   for f in a.fils:
       affiche(f, marge + " ")


affiche(a)


    
