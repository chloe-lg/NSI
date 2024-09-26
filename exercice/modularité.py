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
