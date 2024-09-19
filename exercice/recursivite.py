def fact(n):
    if n== 0:
        return 1
    else: 
        return n * fact(n=1)



def syrase(u):
    print(u)
    if u == 1:
        return None
    elif u % 2 ==0: 
        syrase(u//2)
    else:
        syrase(3*u +1)
    
def serie(n,a,b):
    if n==0:
        return a
    elif n ==1:
        return b
    else:
        return 3* serie(n-1,a,b)+ 2*serie(n-2,a,b)+5

def boucle(i, k):
    if i == k:
        print(i)
    else:
        print(i)
        boucle(i+1,k)

def pgcd(a,b):
    if b ==0:
        return a
    else:
        return pgcd(b, a%b)

assert pgcd(112,90) == 2
print(pgcd(112,90)) 