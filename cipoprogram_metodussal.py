from Cipo import Cipo

def pld_listaban():
    peldany1= Cipo("Nike", 42)
    peldany2= Cipo("Adidas", 41)
    peldany3= Cipo("Adidas", 45)

    cipok=[]
    cipok.append(peldany1)
    cipok.append(peldany2)
    cipok.append(peldany3)
    return cipok

def lista_kiir(lista):
    for i in range(0,len(lista),1):
        marka=lista[i].marka
        meret=lista[i].meret
        print(f"{marka} ({meret})")

#Rövid verzió:
#lista_kiir(pld_listaban())


#Ez a hosszú verzió
cipok_lista=pld_listaban()
lista_kiir(cipok_lista)

def osszegezs_tetele(cipok): #összegzés tétele
    gyujto=0
    for i in range(0,len(cipok),1):
        gyujto+=cipok[i].meret
    atlag=gyujto/len(cipok)
    print(round(atlag,3))

osszegezs_tetele(cipok_lista)

def maxkiv_tetele(cipok): #maximum kiválasztás tétele
    print(f"Milyen márkájú a legnagyobb méretű cipő: ", end="")
    lnm_index=0
    for i in range(0, len(cipok),1):
        if cipok[lnm_index].meret<cipok[i].meret:
            lnm_index=i
    return lnm_index 

lnm_index=maxkiv_tetele(cipok_lista)
print(cipok_lista[lnm_index].marka)

def megszamlalas_tetele(cipok):
    print(f"Hány darab Adidasz cipő van: ", end="")
    szamlalo=0
    for i in range(0,len(cipok),1):
        if cipok[i].marka == "Adidas":
            szamlalo+=1
    print(szamlalo)

megszamlalas_tetele(cipok_lista)

#while-al kéne
def elsontes_tetele(cipok): #eldöntés tétele
    print("Van-e:", end="")
    van = False
    for i in range(0,len(cipok),1):
        if cipok[i].marka=="Adidas" and cipok[i].meret>42:
            van=True
    if van==True:
        print("van 42-nél nagyobb Adidas")
    else:
        print("nincs")
    
elsontes_tetele(cipok_lista)