from pile import Pile, creer_pile


class Historique:
    def __init__(self):
        self.adress_courante = None
        self._adresses_precedentes = creer_pile()
    def aller_a(self, adr):
        if not self.adress_courante is None:
            self._adresses_precedentes.empiler(self.adress_courante)
        self.adress_courante = adr

    
#Test
h = Historique()
assert h.adress_courante is None
h.aller_a("www.stackoverflow.com")
assert h.adress_courante == "www.stackoverflow.com"
h.aller_a("www.developper.com")
h.retour()
assert h.adress_courante == "www.stackoverflow.com"
h.aller_a("")