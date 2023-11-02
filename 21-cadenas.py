
#* Cadenas 
#* Funcion len
word = 'by'
print(len(word)) 
#       ☝️La función len() empleada en las cadenas devuelve el número de caracteres que contiene el argumento
# Ejemplo 2
empty = ''
print(len(empty))
# Ejemplo 3
i_am = 'I\'m'
print(len(i_am))

#* Cadenas multilínea
multiline = """Línea #1
Línea #2"""

print(len(multiline))

#* Operaciones con cadenas 
str1 = 'a'
str2 = 'b'

print(str1 + str2) #esto da una suma de strings ab
print(str2 + str1) #esto da una suma de strings ba
print(5 * 'a')   #esto da una multiplicacion de strings aaaaa
print('b' * 4) # esto da una multiplicacion de strings bbbb


#* Demostración de la función ord ().

char_1 = 'a'
char_2 = ' '  # space

#     ⬇️ ord sirve para saber el valor del punto de código ASCII/UNICODE de un carácter específico
print(ord(char_1))
print(ord(char_2))

#* Demostración de la función chr.

#     ⬇️chr sirve para que Si conoces el punto de código (número) y deseas obtener el carácter correspondiente
print(chr(97))
print(chr(945))

#* Indexando cadenas 
# algunas de caracteristicas de las cadenas se pueden tratasr como una lista

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()

#* Iterando a través de una cadena.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()

#* Rebanadas en las cadenas

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

#* Operadore in 
# comprueba si el argumento izquierdo (una cadena) se puede encontrar en cualquier lugar dentro del argumento derecho (otra cadena).

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)

#* Operador not in
# Si Argumento No se encuentra en la cadena

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)

#* Operaciones con cadenas
# No pienses que la inmutabilidad de una cadena limita tu capacidad de operar con ellas.

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)

#* operador min()
# Ejemplo 1:
print(min("aAbByYzZ"))
#      ☝️Esta función encuentra el elemento mínimo de la secuencia pasada como argumento. 
# Existe una condición - la secuencia (cadena o lista) no puede estar vacía, de lo contrario obtendrás una excepción ValueError.

#  Ejemplo 2 y 3:
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

#*operador max() 
#max() encuentra el elemento máximo de la secuencia.

# Ejemplo 1:
print(max("aAbByYzZ"))


# Ejemplo 2 & 3:
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

#*El método index() 
# es un método, no una función) busca la secuencia desde el principio, para encontrar el primer elemento del valor especificado en su argumento.
# el elemento buscado debe aparecer en la secuencia 
# el índice de la primera aparición del argumento (lo que significa que el resultado más bajo posible es 0, mientras que el más alto es la longitud del argumento decrementado en 1).

# Demonstrando el método index():
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

#*La función list() 
# toma su argumento (una cadena) y crea una nueva lista que contiene todos los caracteres de la cadena, uno por elemento de la lista.
# Demostración de la función list():
print(list("abcabc"))

#*El método count() 
# cuenta todas las apariciones del elemento dentro de la secuencia
# Demostración del metodo count():
print("abcabc".count("b")) 
print('abcabc'.count("d"))