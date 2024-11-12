def validatedni(x):
    
    letraControl=("T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E")
    
    if len(x)!=9:
        return False
    
    if x[0].isdigit(): #DNI
        if not x[:8].isdigit() or not x[8].isalpha():
            return False
        
        numeros = int(x[:8])
        
    elif x[0].upper() in "XYZ": #NIE
        primerDigito={"X":"0","Y":"1","Z":"2"}[x[0].upper()] #Convertir letra en número
        numeros = int(primerDigito+x[1:8]) #Juntar los números
        
        if not x[1:8].isdigit() or not x[8].isalpha():
            return False
        
    else:
        return False
        
    letraFinal = letraControl[numeros%23]
    
    if x[8].upper()==letraFinal:
        return True
    
    return False