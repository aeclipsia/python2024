def validateUser(x):
    if (len(x)<6):
        return False
    
    if (len(x)>12):
        return False
    
    if not x.isalnum():
        return False
    
    return True