class Cellule:
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s

def nieme_element(n, lst):
    while lst is not None:
        if n == 0:
            return lst.valeur
        n-= 1
        lst =lst.suivante
    raise IndexError("indice invalide")
    
def occurences(x, lst):
    if lst is None: 
        return 0
    elif lst.valeur == x:
        return 1 + occurences(x, lst.suivante)
    return occurences(x, lst.suivante)

def occurences_while(x, lst):
    while lst is not None:
        if lst.valeur == x:
            return  1 + lst.suivante
        lst= lst.suivante
    return 0

        

    


    
def concatener(l1, l2):
    if l1 is None:
        return l2
    else:
        return Cellule(l1.valuer, concatener(l1.suivante, l2))