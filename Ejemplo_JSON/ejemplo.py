import json

# with open("Ejemplo_JSON/resources/imagenes.json","r") as fichero:
#     datos=json.load(fichero)
#     print(datos)
#     for row in datos:
#         print("----------------------------------------")
#         for item in row:
#             #print(item[0],":",item[1])
#             print(item , ":" , row[item])
#         print("----------------------------------------")
#     fichero.close()

with open("Ejemplo_JSON/resources/ejemplo.json","r") as x:
    data=json.load(x)
    for row in data:
        print(row,": ",end="{")
        for item in data[row].items():
            print(item[0],":",item[1],end=" ")
        print("}")
    x.close()