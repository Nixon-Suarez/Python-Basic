# platform: permite acceder a los datos de la plataforma subyacente, es decir, hardware, sistema operativo e información sobre la versión del intérprete.
# platform tiene una funcion llamada platform que puede mostrar todas las capas subyacentes en un solo vistazo

from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))

#!import platform           #⬇️terse: cuando se establece a True (o cualquier valor distinto a cero) puede convencer a la función de presentar una forma más breve del resultado 
#!platform(aliased = False, terse = False)
#!           ☝️aliased: cuando se establece a True (o cualquier valor distinto a cero) puede hacer que la función presente los nombres de capa subyacentes alternativos en lugar de los comunes.

#*función machine()
#su utiliza cuando solo se desee conocer el nombre genérico del procesador que ejecuta el sistema operativo junto con Python y el código,

from platform import machine

print(machine())

#*funsion processor() 
# processor() devuelve una cadena con el nombre real del procesador (si lo fuese posible).

from platform import processor

print(processor())

#*función llamada system() 
#system() devuelve el nombre genérico del sistema operativo en una cadena.

from platform import system

print(system())

#* función version().
#La versión del sistema operativo se proporciona como una cadena por la función version().

from platform import version

print(version())

#* funcion python_implementation() y python_version_tuple()
#funciona para ver en que versión de Python está ejecutando tu código 

#                     ⬇️ python_implementation() → devuelve una cadena que denota la implementación de Python (espera CPython aquí, a menos que decidas utilizar cualquier rama de Python no canónica).
from platform import python_implementation, python_version_tuple
#                                               ☝️python_version_tuple() → devuelve una tupla de tres elementos la cual contiene: La parte mayor de la versión de Python. La parte menor. El número del nivel de parche.
print(python_implementation())

for atr in python_version_tuple():
    print(atr)