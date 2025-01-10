import json

with open("Practica Ficheros/Ficheros/series.json","r") as x:
    data=json.load(x)
    print(data)
    for row in data:
        print("-"*50)
        for i in row.items():
            print(i)
    x.close()