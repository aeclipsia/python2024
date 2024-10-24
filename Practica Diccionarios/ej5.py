diccionario={}

def definirDiccionario():
    opD="Y"
    while opD!="N" and opD!="n":
        es=input("Anota palabra en español:\n=>")
        if es in diccionario:
            print("Ya está en el diccionario")
            continue
        
        en=input("Anota su traducción en inglés:\n=>")
        
        diccionario.update({es:en})
        
        opD=input("Quieres añadir más? Y/N\n")
        
def traducir():
    opT="Y"
    while opT!="N" and opT!="n":
        frase=input("Anota la frase o palabra que quieras traducir:\n=>")
        fraselist=frase.split()
        for x in fraselist:
            if x in diccionario:
                translated=diccionario[x]
                frase=frase.replace(x,translated)
        print(frase)
        
        opT=input("Quieres seguir? Y/N\n")

op="0"
while op!="3":
    op=input("Que operación desea hacer:\n1.Definir diccionario\n2.Traducir\n3.Salir\n=>")
    if op=="1":
        definirDiccionario()
        print(diccionario)
    elif op=="2":
        traducir()
    elif op=="3":
        print("programa terminada")
    else:
        print("opción incorrecta")