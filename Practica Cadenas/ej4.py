cadena=input("Anota tu cadena: ")

rev=cadena[::-1]

if cadena==rev:
    print("Palindromo")
else:
    print("No palindromo")