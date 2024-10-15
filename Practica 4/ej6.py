import random

def attackValue():
    return random.randint(1,10)

def defValue():
    return random.randint(1,15)

def attack(attacker,defender):
    defender[2]-=attacker[1]
    print("=>"+attacker[0]+" ha atacado "+defender[0]+"!")
    print(defender[0]+" le queda "+str(defender[2])+" de vida")
    if defender[2]<=0:
        print("****"+attacker[0]+" ha ganado!****")
        return True

n1=input("Anota nombre de P1:\n=>")
n2=input("Anota nombre de P2:\n=>")

p1=[n1,attackValue(),defValue()]
p2=[n2,attackValue(),defValue()]

print("Stats:")
print(p1)
print(p2)

turn=random.randint(0,1)

while p1[2]>0 and p2[2]>0:
    if turn==0:
        attack(p1,p2)
        turn=1
    elif turn==1:
        attack(p2,p1)
        turn=0