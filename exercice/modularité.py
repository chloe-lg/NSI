def cree():
    return [0]*6

def contient(s,x):
    iEntier= x//64
    bit= x%64
    return (s[iEntier] & (1 << bit) !=0)
