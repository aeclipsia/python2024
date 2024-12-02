import csv

def correo1apellido(linea):
    correo1=linea[0]+"."+linea[1]+"@plazacastilla.salesianas.org"
    return correo1.lower()

def correo2apellidos(linea):
    correo2=linea[0]+"."+linea[1]+"."+linea[2]+"@plazacastilla.salesianas.org"
    return correo2.lower()

def existeCorreo(correo):
    with open("Practica Ficheros/Ficheros/AlumnosFP.csv", "r",encoding="latin-1") as fichero:
            doc = list(csv.reader(fichero, delimiter=";"))
            for i in doc[1:]:
                if i[1]==correo:
                    print(i[1]+" ya existe")
                    return True
            return False
            


def addToFile(linea,correo):
    with open("Practica Ficheros/Ficheros/AlumnosFP.csv", "a") as fichero:
        contenido = csv.writer(fichero,delimiter=";")
        nombrecompl=linea[0]+" "+linea[1]+" "+linea[2]
        contenido.writerow([nombrecompl, correo, 'Contra','Creacion propia'])

with open("Practica Ficheros/Ficheros/ListadoAlumnosFP.csv", "r",encoding="latin-1") as fichero:
    doc = list(csv.reader(fichero, delimiter=";"))
    #print(doc)
    
for i in doc[1:]:
    correo1=correo1apellido(i)
    if existeCorreo(correo1):
        correo2=correo2apellidos(i)
        addToFile(i,correo2)
    else:
        addToFile(i,correo1)
        

    
    
