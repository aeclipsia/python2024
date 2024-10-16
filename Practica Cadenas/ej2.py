def first_letter(cadena):
    output=""
    palabras=cadena.split()
    for i in range(len(palabras)):
        output+=(palabras[i])[0]
    print(output)
    
def capitalize(cadena):
    output=""
    palabras=cadena.split()
    for i in range(len(palabras)):
        output+=(palabras[i])[0].upper()+(palabras[i])[1:]+" "
    print(output)
    
def starts_with_a(cadena):
    output=""
    palabras=cadena.split()
    for i in range(len(palabras)):
        if (((palabras[i])[0])=="A")|(((palabras[i])[0])=="a"):
            output+=palabras[i]+" "
    print(output)

first_letter("Universal Serial Bus")
capitalize("republica argentina")
starts_with_a("Antes de ayer")