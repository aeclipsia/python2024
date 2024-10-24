facturas={}
cobrada=0
pendiente=0

def showFactura():
    print("Cobrada: "+str(cobrada)+", Pendiente: "+str(pendiente))

while True:
    op=input("Anota la operación:\n1.Añadir factura\n2.Pagar factura\n3.Terminar\n=>")
    if op == "1":
        numFac=input("Anota el número de factura:\n=>")
        if numFac not in facturas:
            coste=float(input("Anota el coste de la factura:\n=>"))
            facturas.update({numFac:coste})
            
            pendiente+=facturas[numFac]
            
        else:
            print("El número de factura ya está")
            
        showFactura()
    if op=="2":
        pendiente=0
        numFac=input("Anota el número de factura:\n=>")
        if numFac in facturas:
            
            cobrada+=facturas[numFac]
            facturas.pop(numFac)
            
            for p in facturas:
                pendiente+=facturas[p]
            
        else:
            print("El número de factura no está")
            
        showFactura()
    if op=="3":
        break