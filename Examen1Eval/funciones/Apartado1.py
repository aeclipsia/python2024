import csv

empleadosDict={}

def a1(route):
    with open(route,"r",encoding="latin-1") as fichero:
        datos=csv.reader(fichero,delimiter="|")
        for row in datos:
            if row[0] not in empleadosDict:
                empleadosDict.update({row[0]:[row[1]]})
            else:
                if row[1] not in empleadosDict[row[0]]:
                    empleadosDict[row[0]].append(row[1])
        return(empleadosDict)
    
def a2(diccionario):
    print("APARTADO 1")
    for c,v in diccionario.items():
        print(c+" : "+str(v))
    print("-"*50)