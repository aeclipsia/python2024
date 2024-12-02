import csv

def devolverListaDiccionario(fichero):
    datosList = []
    with open(fichero, "r") as fichero_abierto:
        lector = csv.DictReader(fichero_abierto, delimiter=";")
        for fila in lector:
            datosList.append(fila)
    return datosList

def añadirNotaFinal(listaDiccionario):
    for alumno in listaDiccionario:
        try:
            parcial1 = float(alumno['Parcial1'].replace(',', '.'))
        except ValueError:
                parcial1=0
        
        try:    
            parcial2 = float(alumno['Parcial2'].replace(',', '.'))
        except ValueError:
                parcial2=0  
        
        try:
            practicas = float(alumno['Practicas'].replace(',', '.'))
        except ValueError:
                practicas=0  
        
        nota_final = (parcial1 * 0.30) + (parcial2 * 0.30) + (practicas * 0.40)
        
        alumno["NotaFinal"]=round(nota_final,2)
        
    return listaDiccionario

        
def listaAprobadosYSuspensos(listaDiccionario):
    listaSuspensos=[]
    listaAprobados=[]
    for alumno in listaDiccionario:
        try:
            asistencia = float(alumno["Asistencia"].replace('%', '').replace(',', '.'))
            if asistencia == "" or asistencia<75:
                listaSuspensos.append(alumno)
            else: 
                parcial1 = float(alumno["Parcial1"].replace(',', '.'))
                parcial2 = float(alumno["Parcial2"].replace(',', '.')) 
                practicas = float(alumno["Practicas"].replace(',', '.'))
                nota_final = float(alumno["NotaFinal"]) 

                if parcial1 < 4 or parcial2 < 4 or practicas < 4 or nota_final < 5:
                    listaSuspensos.append(alumno)
                else:
                    listaAprobados.append(alumno)
        except ValueError:
            if alumno["Parcial1"]=="":
                alumno["Parcial1"]=0
            if alumno["Parcial2"]=="": 
                alumno["Parcial2"]=0
            if alumno["Practicas"]=="":
                alumno["Practicas"]=0
            listaSuspensos.append(alumno)
    
    return listaSuspensos,listaAprobados

lista_alumnos = devolverListaDiccionario("Practica Ficheros/Ficheros/calificaciones.csv")

lista_alumnos_con_notas = añadirNotaFinal(lista_alumnos)

suspensos, aprobados = listaAprobadosYSuspensos(lista_alumnos_con_notas)

print("Alumnos aprobados:")
for alumno in aprobados:
    print(alumno)

print("\nAlumnos suspensos:")
for alumno in suspensos:
    print(alumno)   
            
            
        
