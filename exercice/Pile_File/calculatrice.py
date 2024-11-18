from pile import Pile


def calculatrice(ep):
    p = Pile()
    tab = ep.split()
    for ele in tab:
        if ele == "*":
            if p.est_vide():
                return None
            a = p.depiler()
            b = p.depiler()
            p.empiler(a * b)


        elif ele == "+":
            if p.est_vide():
                return None
            a = p.depiler()
            b = p.depiler()
            p.empiler(a + b)
        
        else:
            try:
                p.empiler(int(ele))
            except ValueError:
                return None

    return p.depiler()

            
            
      

resul = calculatrice("1 2 3 *  + 4 *")
assert calculatrice("1 2 3 *  + 4 *") == 28
assert calculatrice("1 2 3 *  + 4 +") == 11
assert calculatrice("1 2 3 *  + 4 + -") is None

b = 1