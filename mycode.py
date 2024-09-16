alphab="abcdefghijklmnopqrsuvwxyz"

motsEn= { 
  "a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, 
  "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0,
  "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0
}

def load(fichier):
  """ Fonction qui ouvre le fichier et renvoie le tableau des mots """
  with open(fichier, 'r') as f:
    fichier = [ligne.strip() for ligne in f.readlines()]
  return fichier
  
fichierEn= load("endic.txt")
i=-1
motsEntotal = 0
for ligne in fichierEn :
  if len(ligne) == 1 :
    i+=1
  else : 
    motsEn[alphab[i]]+=1
    motsEntotal+=1
print(motsEn)



def total(dic):
  """on verra"""
  for mot in dic :
    for letre in dic :
      pass