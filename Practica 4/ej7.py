def inTuple(n,tupla):
    for i in tupla:
        if i[0]==n:
            return True
    return False

nombres=list()
nombresFound=list()
while True:
    nombre=input("Anota un nombre:\n=>")
    if nombre=="-1":
        break;
    nombres.append(nombre)

for i in nombres:    
    if inTuple(i, nombresFound):
        continue
    
    x=nombres.count(i)
    
    nombresFound.append((i,x))
        
print(nombresFound)