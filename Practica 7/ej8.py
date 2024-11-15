saludos=['hola','hello','hi']
nombres=['ana','antonio','bea']
    
print([[saludos[i],nombres[n]]for n in range(len(nombres)) for i in range(len(saludos))])