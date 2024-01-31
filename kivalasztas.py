import math

def osztok(szam):
    lista=[]
    oszto=2
    while oszto<=math.sqrt(szam):
        if szam%oszto==0:
            lista.append(oszto)
        oszto+=1
    return lista

"""def osztok(szam):
    lista=[]
    for oszto in range(2, round(math.sqrt(szam)+1)):
        if szam % oszto==0:
            lista.append(oszto)"""

print(osztok[36])