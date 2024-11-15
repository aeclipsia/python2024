import uservalidate.usertest as userVal
import uservalidate.passtest as passVal

userData={}

username=input("Anota usuario: ")
while username!="*":
    if not userVal.validateUser(username) and username!="*" and username not in userData:
        print("Usuario no correcto")
    elif username in userData:
            print("Usuario ya registrado")
    else:
        print("Usuario correcto")
        
        password=input("Anota contraseña: ")
        
        while not passVal.validatePass(password):
            password=input("Anota contraseña: ")
            
        print("Contraseña válida")
        
        userData.update({username:password})
        
    username=input("Anota usuario: ")
    
print(userData)