import uservalidate.usertest as userVal
import uservalidate.passtest as passVal

username=input("Usuario: ")


valid , message=userVal.validateUser(username)

if not valid:
    print(message)
else:
    print("Usuario correcto")
    
password=input("Contraseña: ")

if passVal.validatePass(password):
   print("Contraseña válida") 
else:
    print("La contraseña elegida no es segura")