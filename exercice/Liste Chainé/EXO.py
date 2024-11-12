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
    
def identique(l1, l2):
    if l1 is None and l2 is None:
        return True
    
    if l1 is None or l2 is None:
        return False
    
    
    if l1.valeur == l2.valeur:
        return identique(l1.suivante, l2.suivante)

    else:
        return False

l1 = Cellule(1, Cellule(2, Cellule(3, Cellule(4, None))))
l2 = Cellule(1, Cellule(2, Cellule(3, Cellule(4, None))))

c = identique(l1, l2)

def inserer(x, lst):
    if lst is None:
        return Cellule(x, None)
    elif lst.valeur >= x:
        return Cellule(x, lst)
    else:
        return Cellule(lst.valeur, inserer(x, lst.suivnte))
    