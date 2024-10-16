cadena=input("Anota la cadena:\n=>")
caracter=input("Anota tu caracter:\n=>")

for i in range(len(cadena)):
    if "0"<=cadena[i]<="9":
        cadena=cadena[:i]+caracter+cadena[i+1:]
        
print(cadena)