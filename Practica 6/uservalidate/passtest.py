def validatePass(x):
    
    if len(x)<8 or " " in x:
        return False
    
    tieneMayus=False;
    tieneMinus=False;
    tieneNums=False;
    tieneEspecial=False;
    
    for char in x:
        if char.isupper():
            tieneMayus=True
        elif char.islower():
            tieneMinus=True
        elif char.isdigit():
            tieneNums=True
        elif not char.isalnum():
            tieneEspecial=True
            
        if tieneMayus and tieneMinus and tieneNums and tieneEspecial:
            return True
        
    return False