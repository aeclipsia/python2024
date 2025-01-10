
sitiosList=[]

def a2(route):
    f=open(route,"r")
    f.seek(0)
    for linea in f:
        sitiosList.append(linea[0:-1])
    f.close()
    return sitiosList