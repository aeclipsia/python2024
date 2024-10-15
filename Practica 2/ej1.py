dinero = float(input("Dinero a retirar: "))

comision = (dinero // 100) + 10
print("%s %.2f %s" % ("Dinero a retirar: ",dinero-comision," euros."))
print("%s %.2f %s" % ("Comisión: ",comision," euros"))