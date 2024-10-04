
while True:
    caracter = input("Anota un caracter: ")
    
    if (len(caracter)==1):
        break
    else:
        print("Anota sólo un caracter")

if ('a'<=caracter<='z'):
    print("Es minúscula")
elif ('A'<=caracter<='Z'):
    print("Es mayúscula")
elif ('0'<=caracter<='9'):
    print("Es dígito")