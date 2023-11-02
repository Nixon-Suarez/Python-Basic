from random import * 
#      ☝️#Ofrece algunos mecanismos que permiten operar con números pseudoaleatorios.
#* funcion random 
from random import random
#                   ☝️Este random que es una funcion del modulo random produce un número flotante x entre el rango (0.0, 1.0) - en otras palabras: (0.0 <= x < 1.0).
for i in range(5):
    print(random())

#* funcion seed
from random import random, seed #seed() es capaz de directamente establecer la semilla del generador
# seed() - establece la semilla con la hora actual.
seed(0) ## seed(int_value) - establece la semilla con el valor entero int_value.

for i in range(5):
    print(random())

# *Si deseas valores aleatorios enteros
# una de las siguientes funciones encajaría mejor:
randrange(fin)
randrange(inico, fin)
randrange(inicio, fin, incremento)
randint(izquierda, derecha)
# ej:
from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))
# estas formas implican la posibilidad de numeros repetidos
from random import randint

for i in range(10):
    print(randint(1, 10), end=',')

#* funcion choice
from random import choice, sample
choice(1, 3, 4, 4 ,12) #elige un elemento "aleatorio" de la secuencia de entrada y lo devuelve.
sample(elementos_a_elegir=1) #crea una lista (una muestra) que consta del elemento elementos_a_elegir (que por defecto es 1) "sorteado" de la secuencia de entrada.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # lista de elementos 
#      ⬇️Elige in elemento de my_list
print(choice(my_list))
#      ⬇️Crea una lista aleatoria con el rango en este caso de 5
print(sample(my_list, 5))
print(sample(my_list, 10))

