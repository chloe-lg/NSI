from pile import Pile, cree_pile

def bien_parenthese(chaine):
    pp = Pile()
    pg = Pile()
    for c in chaine:
        if c == '(' :
            pp.empiler(c)  
        elif c == ')':
            if pp.est_vide():
                return False
            po = pp.depiler()
            if po != "(":
                return False
        
        if c == '[' :
            pg.empiler(c)  
        elif c == ']':
            if pg.est_vide():
                return False
            po = pg.depiler()
            if po != "[":
                return False
    return True

            
chaine = "(1 + [3 * 5] + (2 / 6))"

assert bien_parenthese(chaine) == True

a = 1