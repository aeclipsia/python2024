# Implementa una función estaEnLista(letra,lista) -> int
# Recibe una letra y una lista de listas y retorna la posición en la que se encuentra la letra o bien
# -1 si no se encuentra

def estaEnLista(letra,lista):
    for i in range(len(lista)):
        if lista[i][0]==letra:
            return i
    return -1