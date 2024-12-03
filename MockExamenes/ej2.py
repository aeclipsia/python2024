directorio="nif;nombre;email;teléfono;descuento\n01234567;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

lineas=directorio.split("\n")

header=lineas[0].split(";")

diccionario={}

for i in lineas[1::]:
    datos=i.split(";")
    nif=datos[0]
    info={header[x]:datos[x] for x in range(1, len(header))}
    #por cada linea excluida la primera, crear un elemento de forma header(nombre, email, teléfono):dato
    diccionario[nif]=info

print(diccionario)

for clave,valor in diccionario.items():
    print("-"*100)
    print("Cliente -"+clave)
    print(valor)

# for x in diccionario:
#     print("-"*50)
#     print("Cliente -"+x)
#     print(diccionario[x])

#diccionario donde clave principal es NIF y valor una lista de datos que a la vez es un diccionario
#en el subdiccionario las claves son el que está en la primera fila

for x in [1,2,3,4,5]:
    print(x**3)
[x**3 for x in [1,2,3,4,5]]