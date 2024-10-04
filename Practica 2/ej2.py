mes = int(input("Anota el número de un mes: "))

while mes<=0 | mes>12:
    mes = int(input("Debes anotar un número de mes válido: "))
    
fecha31 = (1,3,5,7,8,10,12)
fecha30 = (4,6,9,11)
feb = 2

if mes in fecha31:
    print("Tiene 31 días")
elif mes in fecha30:
    print("Tiene 30 días")
else:
    print("Tiene 28 días")