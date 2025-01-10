from funciones import Apartado1,Apartado2,Apartado3

#rutas
routeCSV="assets/sitios_empleados.csv"
routeTXT="assets/sitios_trabajo.txt"

#Apartado 1
empleadosDict=Apartado1.a1(routeCSV)
Apartado1.a2(empleadosDict)

#Apartado 2a
sitiosList=Apartado2.a2(routeTXT)

#Apartado 2b
nombresList=[c for c,v in empleadosDict.items() for site in v if site not in sitiosList] #list comprehension para guardar los nombres
#quitar nombres duplicados
nombresListNoDuplicates=[]    
[nombresListNoDuplicates.append(i) for i in nombresList if i not in nombresListNoDuplicates]
        
#Imprimir
print("APARTADO 2")
for i in nombresListNoDuplicates:
    print(i)
print("-"*50)

#Apartado 3
sitiosProhibidosDict=Apartado3.generarDict(routeCSV,routeTXT)

print("APARTADO 3")
for c,v in sitiosProhibidosDict.items():
    print(c+" : "+str(v))
print("-"*50)