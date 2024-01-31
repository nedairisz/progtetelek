import math
"""
def osztok(szam):
    lista=[]
    oszto=2
    while oszto<=math.sqrt(szam):
        if szam%oszto==0:
            lista.append(oszto)
        oszto+=1
    return lista

def osztok(szam):
    lista=[]
    for oszto in range(2, round(math.sqrt(szam)+1)):
        if szam % oszto==0:
            lista.append(oszto)

print(osztok[36])"""

def kiv():
    prim=False
    n=9999
    while not prim:
        n+=1
        i=2
        while i<=math.sqrt(n) and n%i!=0:
            i+=1
        prim = i>math.sqrt(n)
    print(n)

kiv()