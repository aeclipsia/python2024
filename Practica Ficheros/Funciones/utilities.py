import os

def writeToFile(route,lista):
    with open(route,"w+") as file:
        for i in lista:
            file.write(i + ", " + lista[i] + "\n")
            
def readFile(route):
    listaTel={}
    if not os.path.exists(route):
        file=open(route,"w+")
        file.close
        
    file=open(route,"r")
    for line in file:
        separated=line[0:-1].split(", ")
        listaTel.update({separated[0]:separated[1]})
    file.close()
    return listaTel