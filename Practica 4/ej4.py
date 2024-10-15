def checkOrdenado(x):
    y=list(x)
    y.sort()
    if x==y:
        print("Está ordenado")
    else:
        print("No está ordenado")

listaOrdenado=[1,2,3,4,5,6,7,8,9,10,11,12]
listaCaos=[1,3,2,4,5,6,7,8,10,12,11,9]

checkOrdenado(listaOrdenado)
checkOrdenado(listaCaos)