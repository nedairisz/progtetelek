import math
#eldontes egy

n = int(input("\nszám: "))
n=int(n)
prim:bool=""
if n<2:
    prim =False
else:
    i=2 
    while i<=math.sqrt(n) and n%i !=0:
        i+=1
    prim= i >math.sqrt(n)
if prim ==True:
    print("prím")
else:
    print("nem prím")