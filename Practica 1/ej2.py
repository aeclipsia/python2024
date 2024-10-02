import math

radius = float(input("Radio de la circunferencia: "))

area = 2 * math.pi * radius

#Formato %.2f significa float con 2 decimales
print("%s %f %s %.2f" % ("Área de la circunferencia con radio",radius,": ",area))