
#* Dir es La función que devuelve una lista ordenada alfabéticamente la cual contiene todos los nombres de las entidades disponibles en el módulo:
import math #importo el modulo

dir(math) # se puede solicitar solamente 

for name in dir(math):  # o hacerlo a travez de un script esto es poco combeniente 
    print(name, end="\t")

