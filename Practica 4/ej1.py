numeros=list()

n=1000
while n>=0:
    n = int(input("Anota un número. Sí quiere salir, anota un número negativo\n=>"))
    if n>0:
        numeros.append(n)

if len(numeros)!=0:
    print("Números pares:")
    for i in range(len(numeros)):
        if numeros[i]%2 == 0:
            print(str(numeros[i]))
    print("El número máximo en la lista es "+str(max(numeros)))
