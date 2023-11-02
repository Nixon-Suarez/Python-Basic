edad = 22

print(edad > 18 and edad < 30) 
#* and (Este opereador pregunta si el primer argumento evalua True, va a preguntar que si el segundo valor Evalua True, si ambos evaluan en True entonces el resultado final va a ser True, si alguno de estos es falso evaluara False )
#     True          True   =  True
#     False         True   =  False 
#     True          False  =  False 
#     False         False  =  False
print(edad > 18 or edad < 30)
#* or (Este operador pregunta si alguna de las dos condiciones es True el resultado final sera True)
#     True          True   =  True
#     False         True   =  True 
#     True          False  =  True 
#     False         False  =  False
print(not True) 
print(not False)
print(not (edad > 17)) #Si es False pasa a True y Si es Trrue pasa a False
#* not (niega lo que esta a la derecha de este)
