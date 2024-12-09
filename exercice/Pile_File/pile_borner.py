class Pile_borner:
    def __init__(self):
        self._contenu = None

    def est_vide(self):
        return self._contenu is None

    def empiler(self, valeur):
        self._contenu = Cellule(valeur, self._contenu)

    def depiler(self):
        if self.est_vide():
            raise IndexError("La pile est vide.")
        valeur = self._contenu.valeur
        self._contenu = self._contenu.suivante
        return valeur
    
def cree_pile(c):
    return Pile()