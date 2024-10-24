diccionario={}

def definirDiccionario():
    while True:
        es=input("Anota palabra en español:\n=>")
        if es in diccionario:
            print("Ya está en el diccionario")
            continue
        
        en=input("Anota su traducción en inglés:\n=>")
        
        diccionario.update({es:en})
        
        op=input("Quieres añadir más? Y/N\n")
        if op=="N" or op=="n":
            break
        
def traducir():
    while True:
        frase=input("Anota la frase o palabra que quieras traducir:\n=>")
        fraselist=frase.split()
        for x in fraselist:
            if x in diccionario:
                translated=diccionario[x]
                frase=frase.replace(x,translated)
        print(frase)
        
        op=input("Quieres seguir? Y/N\n")
        if op=="N" or op=="n":
            break

while True:
    op=input("Que operación desea hacer:\n1.Definir diccionario\n2.Traducir\n3.Salir\n=>")
    if op=="1":
        definirDiccionario()
        print(diccionario)
    elif op=="2":
        traducir()
    else:
        break