def escribirCentrado(t,c="="):
    espacios=40-len(t)//2
    print(" "*espacios+t)
    print(" "*espacios+c*len(t))
    
escribirCentrado("hola")
escribirCentrado("lorem ipsum dolor sit amet, consectetur adipiscing elit","*")