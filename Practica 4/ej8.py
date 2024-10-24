edadLista=list()

n=0
while n!=-1:
    n=int(input("Anota la edad. Pon -1 para salir.\n=>"))
    edadLista.append(n)
    
edadTupla=tuple(edadLista)

for i in range(len(edadTupla)):
    if edadTupla[i]>=20:
        print (edadTupla[i], end="")