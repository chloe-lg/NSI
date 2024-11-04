#Exo 2
def applique(f,t):
    tab= []
    for x in t:
        tab.append(f(x))
    return(tab)

def f(x):
    return x * 2

t= [2, 4]
t2 = applique(f,t)

#Par Compréhension
def applique_comp(f,t):
    return [f(x) for x in t]

t3 = applique_comp(f,t)

#Exo 3
def calcule(op,t, f):
    v =f(t[0])
    for i in range(1, len(t)):
        v= op(v, f(t[i]))
    return v

def op(a, b):
    return a + ", " + b

def f(x):
    return str(x)

t= [1, 2, 3, 4]

rep = calcule(op,t,f)

a=1
