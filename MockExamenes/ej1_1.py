# 1. Implementa una función esVocal(letra) -> bool
# Recibe una letra y determina si es o no un vocal
def esVocal(letra):
    if letra.lower() in 'aeiou':
        return True
    return False

# print(esVocal("a"))
# print(esVocal("b"))
# print(esVocal("A"))
# print(esVocal("B"))