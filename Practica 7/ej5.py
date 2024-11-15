alumnos={"Jared":8,"Alex":10,"Álvaro":3}

listaAprobados=list(filter(lambda x: x[1]>5, alumnos.items()))
print(listaAprobados)

listaSuspensos=list(filter(lambda x: x[1]>5, alumnos.items()))
print(listaSuspensos)

nota=int(input("Anota la nota que quieres buscar:\n=>"))
buscaNota=list(filter(lambda x: x[1]>=nota, alumnos.items()))
print(buscaNota)