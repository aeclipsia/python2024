import random

#Dibujar el boleto
for i in range(0,10):
    for j in range(0,50,10):
        if (i==0) and (j==0):
            print("*", end=" ")
        else:
            print(j+i, end=" ")
    print("|\n", end="")
    
#Pedir al usuario
num=0
numElegidos=list()
while num<6:
    n=int(input("Anota tu número: \n=>"))
    
    if n<=0 | n>49:
        print("Numeros entre 1 y 49 por favor")
        continue
    
    if n in numElegidos:
        print("Ya has elegido ese numero")
        continue
    
    numElegidos.append(n)
    num+=1;
    
#Sorteo
out=0
check=0
while out<6:
    x=random.randint(1,49)
    print("Número "+str(out+1)+": "+str(x))
    if x in numElegidos:
        check+=1
    out+=1
    
if check==4:
    print("3er premio")
elif check==5:
    print("2º premio")
elif check==6:
    print("Bote")
elif check==3:
    print("Reintegro")
else:
    print("Lo siento")