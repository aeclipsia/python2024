def printarFichero(ruta):
    personas=[]
    cabecero=["ID","Nombre","Apellido","Fecha Nacimiento"]
    f=open(ruta,"r")
    for linea in f:
        separado=linea[0:-1].split(";")
        personas.append([{cabecero[x]:separado[x]}for x in range(len(cabecero))])
        
    f.close()
    return personas

personas=printarFichero("Practica Ficheros/Ficheros/personas.txt")

print(personas)

# for i in personas:
#     print(i)