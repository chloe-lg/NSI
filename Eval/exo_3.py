""" EXERCICE 3

1/ Ecrire une classe Date représentant une date avec trois attributs jour, mois et annee (cf tests)

2/ Ajouter une méthode __str__ qui renvoie une chaine de caractères de la forme "25 décembre 2021". On pourra se servir d'un attribut de classe contenant une liste / dictionnaire faisant la correspondance entre le n° du mois stocké dans l'attribut et la chaîne du mois à afficher.

3/ Ajouter une méthode __lt__ qui détermine si une date est antérieure à une autre

"""

# votre classe ICI
    
jour = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
mois = ["janvier", "fevrier", "Mars", "Avirl", "Mai", "Juin", "juillet", "Aout", "Septembre", "octobre", "novembre", "decembre"]
annee =[ 2021, 2022, 2023]


class Date(jour,mois,annee):
    
    def __str__(self):
        return str(jour, mois, annee)
    def __lt__(Date):
        

    

# TESTS
a = Date(12,2,2019)
b = Date(2,12,2019)
assert str(a) == "12 février 2019"
assert str(b) == "2 décembre 2019"

c1 = Date(11,2,2019)
c2 = Date(13,2,2019)
d1 = Date(12,1,2019)
d2 = Date(12,3,2019)
e1 = Date(12,2,2018)
e2 = Date(12,2,2020)
assert c1 < a
assert a < c2
assert d1 < a
assert a < d2
assert e1 < a
assert a < e2

assert not a < c1
assert not c2 < a
assert not a < d1
assert not d2 < a
assert not a < e1
assert not e2 < a

