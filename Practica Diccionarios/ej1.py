cadena=input("Anota una cadena: ")
cadena=cadena.lower()
palabras=cadena.split()

frec={}

for i in palabras:
    if i in frec:
        frec[i]+=1
    else:
        frec[i]=1
        
print(frec)