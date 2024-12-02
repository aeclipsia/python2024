route="Practica Ficheros/Ficheros/texto.txt"

file=open(route,"r")
fullText=[]
for line in file:
    text=line[0:-1].replace(",","")
    text=line[0:-1].replace(".","")
    text=text.upper()
    fullText+=text.split(" ")
    
maxCount=-1000
maxWord=""
for i in fullText:
    count=0
    for j in fullText:
        if i==j:
            count+=1
    if maxCount<count:
        maxCount=count
        maxWord=i
    
            
print("La palabra \""+maxWord+"\" apareció "+str(maxCount)+" veces.")