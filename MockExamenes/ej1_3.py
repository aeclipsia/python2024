# Implementa una función transformar(lista) -> list[ () ]
# Recibe una lista como la del ejemplo del apartado anterior y la transforma en una lista de
# tuplas

def transformar(lista):
    return [tuple(x) for x in lista]

# print(transformar([['a', 1], ['b', 2], ['c', 3]]))