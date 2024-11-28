class Noeud:
    def __init__(self, gauche, valuer, droit):
        self.gauche = gauche
        self.valeur = valeur
        self.droit = droit


def str_arbre(a):
    if a is None: 
        return ""
    return "(" + str_arbre(a.gauche) + a.valeur + str_arbre(a.droit) + ")"
