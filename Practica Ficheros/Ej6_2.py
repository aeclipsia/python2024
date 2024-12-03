import csv

def es_numero_valido(valor):
    """Verifica si un string puede convertirse a número."""
    if not valor or valor.isspace():
        return False
    valor_limpio = valor.replace(',', '.').replace('%', '')
    for c in valor_limpio:
        if not (c.isdigit() or c == '.'):
            return False
    return True

def convertir_nota(valor):
    """Convierte un string de nota a float."""
    if not es_numero_valido(valor):
        return 0.0
    return float(valor.replace(',', '.'))

def convertir_asistencia(valor):
    """Convierte un string de asistencia a float."""
    if not es_numero_valido(valor):
        return 0.0
    return float(valor.replace('%', '').replace(',', '.'))

def devolverListaDiccionario(fichero):
    lista_datos = []
    with open(fichero, "r", encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        cabeceras = next(lector)
        
        for valores in lector:
            alumno = {}
            for i in range(len(cabeceras)):
                alumno[cabeceras[i]] = valores[i]
            lista_datos.append(alumno)
    
    return lista_datos

def addNotaFinal(listaDiccionario):
    for alumno in listaDiccionario:
        parcial1 = convertir_nota(alumno['Parcial1'])
        parcial2 = convertir_nota(alumno['Parcial2'])
        practicas = convertir_nota(alumno['Practicas'])
        
        nota_final = (parcial1 * 0.30) + (parcial2 * 0.30) + (practicas * 0.40)
        alumno["NotaFinal"] = round(nota_final, 2)
    
    return listaDiccionario

def cumple_asistencia_minima(asistencia):
    """Verifica si cumple el requisito de asistencia mínima."""
    return asistencia >= 75

def tiene_notas_minimas(parcial1, parcial2, practicas):
    """Verifica si todas las notas parciales superan el mínimo de 4."""
    return parcial1 >= 4 and parcial2 >= 4 and practicas >= 4

def tiene_nota_final_aprobada(nota_final):
    """Verifica si la nota final es aprobada (≥5)."""
    return nota_final >= 5

def esta_aprobado(alumno):
    """Determina si un alumno está aprobado según todos los criterios."""
    asistencia = convertir_asistencia(alumno["Asistencia"])
    parcial1 = convertir_nota(alumno["Parcial1"])
    parcial2 = convertir_nota(alumno["Parcial2"])
    practicas = convertir_nota(alumno["Practicas"])
    nota_final = alumno["NotaFinal"]
    
    if not cumple_asistencia_minima(asistencia):
        return False
    
    if not tiene_notas_minimas(parcial1, parcial2, practicas):
        return False
    
    if not tiene_nota_final_aprobada(nota_final):
        return False
    
    return True

def listaAprobadosYSuspensos(listaDiccionario):
    listaSuspensos = []
    listaAprobados = []
    
    for alumno in listaDiccionario:
        if esta_aprobado(alumno):
            listaAprobados.append(alumno)
        else:
            listaSuspensos.append(alumno)
    
    return listaSuspensos, listaAprobados

lista_alumnos = devolverListaDiccionario("Practica Ficheros/Ficheros/calificaciones.csv")
lista_alumnos_con_notas = addNotaFinal(lista_alumnos)
suspensos, aprobados = listaAprobadosYSuspensos(lista_alumnos_con_notas) 
print("Alumnos aprobados:")
for alumno in aprobados:
    print(alumno)
    
print("\nAlumnos suspensos:")
for alumno in suspensos:
    print(alumno)