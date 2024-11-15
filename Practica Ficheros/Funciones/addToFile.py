def addToFile(route,lista):
    with open(route,"w+") as file:
        for i in lista:
            file.write(i + ", " + lista[i] + "\n")