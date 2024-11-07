def validateUser(x):
    if (len(x)<6):
        return False, "El nombre de usuario debe contener al menos 6 carácteres"
    
    if (len(x)>12):
        return False, "El nombre de usuraio no debe contener más de 12 carácteres"
    
    if not x.isalnum():
        return False, "El nombre de usuario puede contener sólo letras y números"
    
    return True, ""