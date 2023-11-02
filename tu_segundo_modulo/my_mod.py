#!/usr/bin/env python3  
#☝️#!: en python indica al sistema operativo como ejecutar el contenido del archivo (en otras palabras, que programa debe ejecutarse para interpretar el texto).

""" module.py - Un ejemplo de un módulo en Python """

__counter = 0


def suml(the_list): # Funcion suml
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list): # Funcion prodl
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod

#     ⬇️Se ha utilizado la variable __name__ para detectar cuando se ejecuta el archivo de forma independiente, y se aprovechó esta oportunidad para realizar algunas pruebas sencillas.
if __name__ == "__main__":
    print("Yo prefiero ser un módulo, pero puedo realizar algunas pruebas por ti")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)

