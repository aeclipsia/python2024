def filtrar_palabras(lista,letras):
    for i in range(len(lista)):
        if len(lista[i])>=letras:
            print(lista[i])
            
original=["En", "la", "granja", "la", "vaca", "pasea", "tranquila", "por", "el", "prado", "disfrutando", "del", "sol"]

filtrar_palabras(original,6)