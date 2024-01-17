from Cipo import Cipo


peldany1= Cipo("Nike", 42)
peldany2= Cipo("Adidas", 41)
peldany3= Cipo("Adidas", 45)

cipok=[]
cipok.append(peldany1)
cipok.append(peldany2)
cipok.append(peldany3)

for i in range(0,len(cipok),1):
    marka= cipok[i].marka
    meret=cipok[i].meret
    print(f"{marka} ({meret})")

def meret_atlag(cipok):
    gyujto=0
    for i in range(0,len(cipok),1):
        gyujto+=cipok[i].meret
        print(round(gyujto/len(cipok),3))

meret_atlag(cipok)


#while-al kéne
def nagyobb42adidas(cipok):
    print("Van-e:", end="")
    van = False
    for i in range(0,len(cipok),1):
        if cipok[i].nev=="Adidas" and cipok[i].meret>42:
            van=True
    if van==True:
        print("van")
    else:
        print("nincs")
    
nagyobb42adidas()