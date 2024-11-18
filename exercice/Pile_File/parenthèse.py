from pile import Pile 

def parenthese_correspondante(ep, f):
  p = cree_pile() 
  i = 0  

  while i < len(ep): 
        if ep[i] == '(':
            p.empiler(i)  
        elif ep[i] == ')':
            if p.est_vide():
                raise ValueError("Expression mal parenthésée.")
            indice_ouvrante = p.depiler() 
            if i == f: 
                return indice_ouvrante
        i += 1  

    raise ValueError("Indice de parenthèse fermante non valide ou expression mal formée.")
  
ep = "(a + (b * c) + (d / e))"

try:
    # Tests valides
    assert parenthese_correspondante(ep, 7) == 3  
    assert parenthese_correspondante(ep, 17) == 10  

    # Test invalide
    try:
        parenthese_correspondante(ep, 0)  
    except ValueError as e:
        assert str(e) == "Indice de parenthèse fermante non valide ou expression mal formée."

    print("Tous les tests sont passés !")

except AssertionError:
    print("Test a échoué.")
