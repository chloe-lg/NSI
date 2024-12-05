""" EXERCICE 2

1/ Ecrire une fonction  derniere_cellule(lst)  qui renvoie la dernière cellule de la liste chainée  lst  . On suppose la liste  lst  non vide.


2/ Ecrire une fonction  concatener_en_place(l1, l2)  qui réalise une concaténation en place des listes l1 et l2, c'est-à-dire qui relie la dernière cellule de l1 à la première cellule de l2. Cette fonction doit renvoyer la première cellule de la liste concaténée.

"""
class Cellule:
    """une cellule d'une liste chaînée"""
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s

# votre fonction   derniere_cellule   ICI

def derniere_cellule(lst):
    while lst is not None:
        v = lst.suivante
        return v

# votre fonction   concatener_en_place(l1, l2)   ICI

def concatener_en_place(l1, l2):
    if l1 is None:
        return l2
    else:
        return derniere_cellule(l1.valeur, concatener_en_place(l2.suivante, l1))



# 2 fonctions utilitaires pour les (ou vos) tests
def str_liste(lst):
    """renvoie une chaine de caractère représentant les valeurs de la liste lst"""
    if lst is None:
        return "\n"
    else:
        return str(lst.valeur) + ", " + str_liste(lst.suivante)

def identiques(l1, l2):
    """renvoie un booléen indiquant si les listes sont composées des mêmes valeurs dans le même ordre"""
    if l1 is None:
        return l2 is None
    elif l2 is None:
        return l1 is None
    else:
        return l1.valeur == l2.valeur and identiques(l1.suivante, l2.suivante)

# TESTS
a = Cellule("toto", None)
assert derniere_cellule(a).valeur == "toto"
b = Cellule(1, Cellule(2, Cellule(5, Cellule(8, None))))
assert derniere_cellule(b).valeur == 8

l1 = Cellule(3, Cellule(4, Cellule(5, None)))
assert identiques(l1, concatener_en_place(None, l1))
l2 = Cellule(1, Cellule(2, None))
l3 = Cellule(1, Cellule(2, Cellule(3, Cellule(4, Cellule(5, None)))))
assert identiques(l3, concatener_en_place(l2, l1))

h = 1

