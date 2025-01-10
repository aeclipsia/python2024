from modelos import *

op=input("1.Añadir Contacto\n2.Buscar Contacto\n3.Listar Contactos\n4.Eliminar Contactos\n*.Salir\n=> ")
while op!="*":
    if op=="1":
       nombre=input("Anota su nombre: ")
       tel=input("Anota su telefono: ")
       email=input("Anota su email: ")
    
    add = Agenda.add(nombre,tel,email)
    if add:
        print("Contacto agregado correctamente")
    else:
        print("El número de telefono ya existe")
       
    op=input("1.Añadir Contacto\n2.Buscar Contacto\n3.Listar Contactos\n4.Eliminar Contactos\n*.Salir\n=> ")