import csv

currentData={}
pendingData={}
with open("Practica Ficheros/Ficheros/AlumnosFP.csv","r",encoding="latin-1") as fichero:
    datos=csv.reader(fichero,delimiter=";")
    next(datos)
    for row in datos:
        currentData.update({row[0]:[row[1],row[2],row[3]]})
        
with open("Practica Ficheros/Ficheros/ListadoAlumnosFP.csv","r",encoding="latin-1") as fichero:
    datos=csv.reader(fichero,delimiter=";")
    next(datos)
    for row in datos:
        pendingData.update({row[0]:[row[1],row[2]]})

# for data in currentData.items():
#     print(data[0])
#     print(data[1][0])
    
print(currentData.keys())
    
for data in pendingData.items():
    fullName=str(data[0])+" "+str(data[1][0])+" "+str(data[1][1])
    if fullName in currentData.keys():
        print(fullName)
    # print(str(data[0]).lower()+"."+str(data[1][0]).lower()+"@plazacastilla.salesianas.org")