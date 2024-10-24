def inTuple(n,tupla):
    for i in tupla:
        if i[0]==n:
            return True
    return False

nombres=list()
nombresFound=list()
nombre="0"
while nombre!="-1":
    nombre=input("Anota un nombre:\n=>")
    if nombre=="-1":
        print("programa terminada")
        break
    nombres.append(nombre)

for i in nombres:    
    if inTuple(i, nombresFound):
        continue
    
    x=nombres.count(i)
    
    nombresFound.append((i,x))
        
print(nombresFound)