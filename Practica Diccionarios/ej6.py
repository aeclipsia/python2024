facturas={}

cobrada=0

def sumPendiente():
    list_pendientes=[]
    for i in facturas:
        list_pendientes.append(facturas[i])
    pendiente=sum(list_pendientes)
    return pendiente

def showFactura():
    print("Cobrada: "+str(cobrada)+", Pendiente: "+str(sumPendiente()))


op="0"
while op!="3":
    print(facturas)
    showFactura()
    
    op=input("Anota la operación:\n1.Añadir factura\n2.Pagar factura\n3.Terminar\n=>")
    if op == "1":
        numFac=input("Anota el número de factura:\n=>")
        if numFac not in facturas:
            coste=float(input("Anota el coste de la factura:\n=>"))
            facturas.update({numFac:coste})
            
        else:
            print("El número de factura ya está")
    elif op=="2":
        numFac=input("Anota el número de factura:\n=>")
        if numFac in facturas:
            
            cobrada+=facturas[numFac]
            
            facturas.pop(numFac)
            
        else:
            print("El número de factura no está")
    elif op=="3":
        print("programa terminada")
    else:
        print("opción incorrecta")