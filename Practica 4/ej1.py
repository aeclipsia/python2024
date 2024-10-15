numeros=list()

while True:
    n = int(input("Anota un número. Sí quiere salir, anota un número negativo\n=>"))
    numeros.append(n)
    if n<0:
        break
    
print("Números pares:")
for i in range(len(numeros)):
    if numeros[i]%2 == 0:
        print(str(numeros[i]))

print("El número máximo en la lista es "+str(max(numeros)))
