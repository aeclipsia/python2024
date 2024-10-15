original=["En", "la", "granja", "la", "vaca", "pasea", "tranquila", "por", "el", "prado", "disfrutando", "del", "sol"]

cadena=input("Anota la cadena:\n=>")

presentCount=0

try:
    original.index(cadena)
except:
    print("***cadena no encontrada***")
    exit
    
for i in range(len(original)):
    if original[i]==cadena:
        presentCount+=1
        
print("La cadena \""+cadena+"\" apareció "+str(presentCount)+" veces.")

palabraNueva=input("Anota la cadena para reemplazar \""+cadena+"\":\n=>")

for i in range(len(original)):
    if original[i]==cadena:
        original[i]=palabraNueva
    
    print(original[i], end=" ")