import random
from colorama import Fore

#print (Fore.RED+"Rojo"+Fore.BLUE+"BLUE")

#Generador
colors=("R", "A", "Z", "V", "W", "B", "F")
ficha=list()

while True:
    x=random.choice(colors)
    
    if (ficha.count(x)<2):
        ficha.append(x)
    
    if (len(ficha)>=5):
        break
    
print(ficha)

tries=6
    

while True:
    countCorrect=0
    
    print("Tienes "+str(tries)+" intentos")
    propo=[i for i in input(Fore.WHITE+"Propone la combinación:\n=>")]
    tries-=1
    
    for m in range(len(propo)):
        if propo[m]==ficha[m]:
            countCorrect+=1
            
            if propo[m]=="R":
                print(Fore.RED+propo[m], end="")
            elif propo[m]=="A":
                print(Fore.YELLOW+propo[m], end="")
            elif propo[m]=="Z":
                print(Fore.BLUE+propo[m], end="")
            elif propo[m]=="V":
                print(Fore.GREEN+propo[m], end="")
            elif propo[m]=="W":
                print(Fore.WHITE+propo[m], end="")
            elif propo[m]=="B":
                print(Fore.LIGHTWHITE_EX+propo[m], end="")
            elif propo[m]=="F":
                print(Fore.MAGENTA+propo[m], end="")
        elif propo[m] in ficha:
            print(Fore.LIGHTRED_EX+"O", end="")
        else:
            print(Fore.BLACK+"X", end="")
    print("\n")
    
    if countCorrect==5:
        print(Fore.WHITE+"Adivinaste!")
        break
    
    if tries==0:
        print("No lo adivinaste, la ficha es: ", end="")
        for i in ficha:
            if i=="R":
                print(Fore.RED+i, end="")
            elif i=="A":
                print(Fore.YELLOW+i, end="")
            elif i=="Z":
                print(Fore.BLUE+i, end="")
            elif i=="V":
                print(Fore.GREEN+i, end="")
            elif i=="W":
                print(Fore.WHITE+i, end="")
            elif i=="B":
                print(Fore.LIGHTWHITE_EX+i, end="")
            elif i=="F":
                print(Fore.MAGENTA+i, end="")
        print("\n")
        break