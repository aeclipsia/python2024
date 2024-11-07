def validatePass(x):
    
    if len(x)<8:
        return False
    
    lower=x.islower() #tiene que ser False
    caps=x.isupper()
    nums=x.isdigit()
    symbols=x.isalnum()
    
    space=False
    
    for i in x:
        if i.isspace():
            space=True
            
    # print(lower)
    # print(caps)
    # print(nums)
    # print(symbols)
    # print(space)
            
    if ~lower and ~caps and ~nums and ~symbols and space:
        return True
    
    return False