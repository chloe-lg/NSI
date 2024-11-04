def cree():
    return [0]*6

def contient(s,x):
    iEntier= x//64
    bit= x%64
    return (s[iEntier] & (1 << bit) !=0)

def ajoute(s,x):
    iEntier= x//64
    bit= x%64
    s[iEntier] = s[iEntier] | 1<<bit

def enumere(s):
    tab = []
    a = 0
    for e in s:
        for i in range(64):
            if e & (1 << i) !=0: 
                tab.append(i + a*64)
        a += 1
    return tab

def tranche(t,i,j):
    tab= []
    if j <= i:
        return []
    for x in range(i,j):
        tab.append(t[x])

def concatenation(t1,t2):
    t3=[]
    for x in t1:
        t3.append(x)
    for x in t2:
        return t3


