from Funciones import utilities

routeLista="Practica Ficheros/Ficheros/listin.txt"
listaTel=utilities.readFile(routeLista)
nombre=input("Anota su nombre. (* para salir)\n=>")

def buscar(listaTel, nombre, borrar=False):
    encontrado=False
    for i in listaTel:
        if i==nombre:
            encontrado=True
            if borrar==True:
                listaTel.pop(i)
                break
            else:
                print("Telefono del usuario "+nombre+": "+listaTel[i])
            
    if encontrado==False:
        print("Usuario "+nombre+" no encontrado")

while nombre!="*":
    if nombre=="":
        print("Nombre está vacio")
    elif nombre.isalpha()==False:
        print("Formato incorrecto")
    else:
        ope=int(input("-"*50+"\n1.Añadir\n2.Consultar\n3.Eliminar\n"))
        if ope==1:
            telefono=input("Anota su telefono\n=>")
            while telefono=="" or telefono.isdigit()==False:
                print("Telefono incorrecto")
                telefono=input("Anota su telefono\n=>")
            print(nombre,":",telefono)
            listaTel.update({nombre:telefono})
        elif ope==2:
            buscar(listaTel, nombre)
        
        elif ope==3:
            buscar(listaTel, nombre, True)
                    
    nombre=input("Anota su nombre (* para salir)\n=>")
utilities.writeToFile(routeLista,listaTel)