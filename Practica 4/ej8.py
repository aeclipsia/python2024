edadLista=list()

while True:
    n=int(input("Anota la edad. Pon -1 para salir.\n=>"))
    if n==-1:
        break
    edadLista.append(n)
    
edadTupla=tuple(edadLista)

for i in range(len(edadTupla)):
    if edadTupla[i]>=20:
        print (edadTupla[i], end="")