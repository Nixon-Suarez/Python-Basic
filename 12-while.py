lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"]

i = 1 # i: valor inicial
while i <= 5: # el bucle se ejecuta si se cumple la condicion 
    print(i)
    i = i + 1 # Condicion de salida sino se pone se ejecutara infinitamente 
#   se evalua hasta se deje de cumplir la condicion inicial en este caso i <= 5

i = 1 
while i <= 5: 
    print(i * "Holaaaa ") # tambien se puede utilizar con un string 
    i = i + 1

i = 0
while i < len(lenguajes): # Accede a los datos de un listado 
    print(lenguajes[i])
    i = i + 1


