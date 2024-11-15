listaTel={}


nombre=input("Anota su nombre. (* para salir)\n=>")
while nombre!="*":
    if nombre=="":
        print("Vacio")
    elif nombre.isalpha()==False:
        print("Formato incorrecto")
    else:
        telefono=input("Anota su telefono\n=>")
        while telefono=="" or telefono.isdigit()==False:
            print("Telefono incorrecto")
            telefono=input("Anota su telefono\n=>")
        print(nombre,":",telefono)
        listaTel.update({nombre:telefono})
    nombre=input("Anota su nombre (* para salir)\n=>")

with open("Practica Ficheros/Ficheros/listin.txt","w+") as file:
    for i in listaTel:
        file.write(i + ", " + listaTel[i] + "\n")
        