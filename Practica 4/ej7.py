nombres=list()
nombresFound=list()
while True:
    nombre=input("Anota un nombre:\n=>")
    if nombre=="-1":
        break;
    nombres.append(nombre)

maximo=-1000

for i in nombres:
    buscar=i
    
    if i in nombresFound:
        continue
    
    nombresFound.append(i)
    x=0

    for j in nombres:
        if buscar==j:
            x+=1
    print(buscar+": "+str(x))
    
    if maximo<x:
        maximo=x