#Exercice 1
class Chrono:
    heure_max= 24
    def __init__(self, h, m, s) -> None:
        self._temps = 3600*h + 60*m + s

    def avance(self, s):
        self._temps += s

    def _conversion(self):
        s = self._temps
        return (s // 3600, (s // 60) % 60, s % 60)

    def __str__(self) -> str:
        h, m, s = self._conversion()
        return (str(h) +"h" + str(m) +"m" +str(s) + "s")
    
    def __eq__(self, t) -> bool:
        return (self. _temps == t._temps )
    
    