nombres=list()
while True:
    nombre=input("Anota un nombre:\n=>")
    if nombre=="-1":
        break;
    nombres.append(nombre)

maximo=-1000

for i in range(len(nombres)):
    buscar=nombres[i]
    x=0
    
    if buscar==nombres[i-1]:
        continue
    
    for j in range(len(nombres)):
        if buscar==nombres[j]:
            x+=1
    print(buscar+": "+str(x))
    
    if maximo<x:
        maximo=x