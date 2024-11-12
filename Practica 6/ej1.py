import uservalidate.usertest as userVal
import uservalidate.passtest as passVal

userData={}

username=input("Anota usuario: ")
while username!="*":
    while not userVal.validateUser(username) and username!="*" and username not in userData:
        if username in userData:
            print("Usuario ya registrado")
        
        username=input("Anota usuario: ")
    
    if username=="*":
        break
    
    print("Usuario correcto")
    
    password=input("Anota contraseña: ")
    
    while not passVal.validatePass(password):
        password=input("Anota contraseña: ")
        
    print("Contraseña válida")
    
    userData.update({username:password})
    
    username=input("Anota usuario: ")
    
print(userData)