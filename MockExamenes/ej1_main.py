# Leer una cadena y generar una lista de tuplas con las veces que cada vocal se repite ordenada de
# mayor a menor frecuencia.

from ej1_1 import esVocal
from ej1_2 import estaEnLista
from ej1_3 import transformar

cadena=input("Anota la cadena:\n=>").upper()
resLista=[]
for i in cadena:
    if esVocal(i):
        x = estaEnLista(i,resLista)
        if x!=-1: #si está en la lista, se suma 1 en su frecuencia
            resLista[x][1]+=1
        else: #si no está, se añade en la lista
            resLista.append([i,1])

resTuple=transformar(resLista) #Transforma la lista de listas en lista de tuples
resTuple.sort(key=lambda x:x[1],reverse=True) #apartado 4
print(resTuple)