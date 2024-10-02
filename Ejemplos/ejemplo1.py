#No usar ; y las variables no se tipifican
nombre = 'Rosa' 
numero = 5
print(type(nombre))
print(type(numero))

test_substring = '28034'
print(test_substring)
#substring tiene sintaxis [i:j:k] donde i es igual a la posición donde empieza, j la posición final -1 y k el intervalo

#ciudad 28
print(test_substring[0:2])
#municipio 0
print(test_substring[2]) #o igual a [2:3]
#poblacion 34
print(test_substring[-2:]) #-2: saca los 2 últimos mientras :-2 saca todo menos los 2 últimos

#chr nos devuelve su código ASCII
print(chr(1006))
#ord devuelve el contrario
print(ord("a"))

#conversiones:
a = int("333")
b = float("256.56")
c = complex("1+2j")

#operadores ++ y -- no existen pero += y -= sí

#existe asignación múltiple
name, age, weight = "Jared", 22, 70
print(name)
print(age)
print(weight)

#operadores de identidad is e isnot
x = 5
y = x
print(x is y)
y = y + 1
print(x is y)
print(y is 6)

#operadores aritmétics
# + suma, - resta, * multiplica, / división (float), // división (int), % módulo, ** potencia

#operadores de comparación a nivel de bit
# x | y OR, x ^ y XOR, x & y AND, x << n desplazamiento a la izquierda n bits,
# x >> n desplazamiento a la izquierda n bits, ~x devuelve los bits invertidos

#operadores lógicos
# x or y, x and y, not x

#existe funciones all(iterador) y any(iterador)

#para concatenar una cadena se usa + y * n para repetir n veces

#operadores de pertenencia
#in y not in

#objetos inmutables
n = 5
print(id(n))
print(id(5))

m = 5
print(id(m))

#LAS CADENAS SON INMUTABLES!

#lee entradas con input (en string)