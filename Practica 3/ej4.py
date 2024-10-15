def convertirEspaciado(texto,cantidad=1):
    for i in range(len(texto)):
        print(texto[i],end=" "*cantidad)
        
convertirEspaciado("Hola mundo")