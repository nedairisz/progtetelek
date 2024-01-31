def kerese():
    also=42
    felso=67
    i=also
    while i<=felso and not(i%10==0):
        i+=1
    van:bool=i<=felso
    if van:
        print(f"van 0-ra végződő szám: {i}")
    else:
        print("nincs 0-ra véhződő szám")

kerese()