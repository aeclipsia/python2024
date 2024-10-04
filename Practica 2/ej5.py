import math
import random

x = random.randint(1,10)
tries = 0

while tries<5:
    y = int(input("Adivina mi número!\t"))
    
    tries+=1
    
    if (y<x):
        print("Mi número es mayor que "+str(y))
    elif (y>x):
        print("Mi número es menor que "+str(y))
    else:
        print("Enhorabuena! Adivinaste mi número en "+str(tries)+" intentos! Es el número "+str(x))
        break
    
print("No lo adivinaste dentro de 5 intentos. Mi número es "+str(x))