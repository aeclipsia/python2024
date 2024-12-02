import os

route="Practica Ficheros/Ficheros/contador.txt"

def modifyCount(mode):
    file=open(route,"r+")
    for line in file:
        if mode=="inc":
            current=str(int(line)+1)
        elif mode=="dec":
            current=str(int(line)-1)
    file.seek(0)
    file.write(current)
    return current

def count(inc=0,dec=0):
    current=0    
    if not os.path.exists(route):
        file=open(route,"w+")
        file.write("0")
        file.close
        
    if inc==0 and dec==0:
        empty=True
        
        file=open(route,"r+")
        for line in file:
            if line.strip():
                current=line
                empty=False
        
        if empty:
            file.write("0")
            
        return current
    
    if inc!=0 and dec==0:
        return modifyCount("inc")
        
    if inc==0 and dec!=0:
        return modifyCount("dec")
        
op=int(input("0.Salir\n1.Mostrar\n2.Incrementar\n3.Decrementar\n=>"))
while op!=0:
    if op==1:
        print(count())
    elif op==2:
        print(count(inc=1))
    elif op==3:
        print(count(dec=1))
    op=int(input("0.Salir\n1.Mostrar\n2.Incrementar\n3.Decrementar\n=>"))