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
