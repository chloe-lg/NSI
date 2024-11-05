class Cellule:
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s

class Liste:
    def __init__(self):
        self._tete = None
    
    def est_vide(self):
        return self._tete is None
    
    def ajoute(self,x):
        self._tete = Cellule(x, self._tete)

    def __len__(self):
        n = 0
        c = self._tete
        while c is not None:
            n+= 1
            c = c.suivante
        return n
    def __getitem__(self,n):
        return nieme_element(n, self._tete)
    
    def renverser(self):
        self._tete = renverser(self._tete)
        