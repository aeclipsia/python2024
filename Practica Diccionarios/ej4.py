diccionario_gustos={"Alex":["locowin","cerveza"]}

def checkName(p):
    if p in diccionario_gustos:
        print("Está en la lista")
        return True
    return False

def checkLikes(g,l):
    if g in l:
        print("Está en los gustos")
        return False
    return True

while True:
    g=input("Añadir gusto\n=>")
    p=input("A quién?\n=>")
    
    if (checkName(p)):
        lista_gustos=diccionario_gustos[p]
        if (checkLikes(g,lista_gustos)):
            lista_gustos.append(g)
        else:
            print("Ya está en la lista de gustos de "+p)
    else:
        diccionario_gustos.update({p:[g]})
    
    ope=input("Quieres añadir más? Y/N\n=>")
    if ope=="N" or ope=="n":
        break
            
for i in diccionario_gustos:
    print("nombre"+i)
    print("gustos:",end="")
    for j in diccionario_gustos[i]:
        print(j, end=",")
    print("\n") 