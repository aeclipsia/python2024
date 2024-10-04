import math
import random

x = random.randint(1,10)

while True:
    y = int(input("Adivina mi número!\t"))
    
    if (y<x):
        print("Mi número es mayor que "+str(y))
    elif (y>x):
        print("Mi número es menor que "+str(y))
    else:
        print("Enhorabuena! Adivinaste mi número! Es el número "+str(x))
        break