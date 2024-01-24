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

def meret_atlag(cipok): #összegzés tétele
    gyujto=0
    for i in range(0,len(cipok),1):
        gyujto+=cipok[i].meret
        print(round(gyujto/len(cipok),3))

meret_atlag(cipok)

def lnc_markaja(cipok): #maximum kiválasztás tétele
    print(f"Milyen márkájú a legnagyobb méretű cipő: ", end="")
    lnm_index=0
    for i in range(0, len(cipok),1):
        if cipok[lnm_index].meret<cipok[i].meret:
            lnm_index=i
    return lnm_index 

lnm_index=lnc_markaja(cipok)
print(cipok[lnm_index].marka)

def hany_adi(cipok):
    print(f"Hány darab Adidasz cipő van: ", end="")
    szamlalo=0
    for i in range(0,len(cipok),1):
        if cipok[i].marka == "Adidas":
            szamlalo+=1
    print(szamlalo)

hany_adi(cipok)

#while-al kéne
def nagyobb42adidas(cipok): #eldöntés tétele
    print("Van-e:", end="")
    van = False
    for i in range(0,len(cipok),1):
        if cipok[i].marka=="Adidas" and cipok[i].meret>42:
            van=True
    if van==True:
        print("van 42-nél nagyobb Adidas")
    else:
        print("nincs")
    
nagyobb42adidas(cipok)