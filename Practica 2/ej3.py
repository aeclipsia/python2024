
caracter="xx"
while len(caracter)!=1:
    caracter = input("Anota un caracter: ")
    
    if (len(caracter)!=1):
        print("Anota sólo un caracter")

#if (caracter>='a') & (caracter<='z'):
#if (caracter>='a' and caracter<='z'):
if ('a'<=caracter<='z'):
    print("Es minúscula")
elif ('A'<=caracter<='Z'):
    print("Es mayúscula")
elif ('0'<=caracter<='9'):
    print("Es dígito")
else:
    print("Es un simbolo")