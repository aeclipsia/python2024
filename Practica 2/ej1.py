dinero = float(input("Dinero a retirar: "))

multiplicador = (dinero // 1000) + 1

print("%s %.2f %s" % ("Comisión: ",10*multiplicador," euros"))