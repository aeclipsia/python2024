from funciones import Apartado2
import csv

def checkSitios(aux,site):
    for c,v in aux.items():
        if site[0]==c:
            if site[1]==v[0][0]:
                v[0][1]=str(int(v[0][1])+int(site[2]))
            else:
                v.append([site[1],site[2]])
            

def sacarEmpleadosDict(route):
    aux={}
    with open(route,"r",encoding="latin-1") as fichero:
        datos=csv.reader(fichero,delimiter="|")
        for row in datos:
            if row[0] not in aux:
                aux.update({row[0]:[[row[1],row[2]]]})
            else:
                checkSitios(aux,row)            
        return aux

def generarDict(routeCSV,routeTXT):
    
    empleadosDict=sacarEmpleadosDict(routeCSV)
    sitiosList=Apartado2.a2(routeTXT)
    
    sitiosNotValidDict={}
    for c,v in empleadosDict.items():
        for site in v:
            if site[0] not in sitiosList:
                if c in sitiosNotValidDict:
                    sitiosNotValidDict[c].append(site)
                else:
                    sitiosNotValidDict.update({c:[site]})

    return sitiosNotValidDict