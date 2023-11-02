from my_mod import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

from sys import path

path.append('..\\modules') # si el modulo no esta en la misma carpeta puedes utilizar la ruta absoluta ➡️ path.append('C:\\Users\\user\\py\\my_mod')

import my_mod

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(my_mod.suml(zeroes))
print(my_mod.prodl(ones))


