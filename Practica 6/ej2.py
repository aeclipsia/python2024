import datavalidate.dnitest as dniVal
import datavalidate.edadtest as edadVal

dni=input("Anota tu dni:\t")
if dniVal.validatedni(dni):
    print("DNI Válido")
else:
    print("DNI no válido")
    
edad=input("Anota tu edad:\t")
if not edadVal.validateAge(edad):
    print("Eres menor")
else:
    print("¡Qué mayor!")