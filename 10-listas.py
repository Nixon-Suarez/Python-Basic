# las listas sirven para guardar varias variables dentro de una sola

lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"]
#               0         1       2       3            4           
print(lenguajes[1]) #Selecciona el argumento 1 (Ruby)
lenguajes [1]= "Go" # Reemplaza el argumento 1 (Ruby) por "Go"
print(lenguajes[-1]) # al indicar numeros negativos toma en cuenta el argumento primero pero de atras para adelante en este caso seria Java
print(lenguajes[1:3]) # : indican un rango de elementos dentro del lisitado
# en este caso desde el elemento 1 hasta el elemento 3 (Solo aparecen los elementos que estan detro de este rango no aparecen los que determinan el rango)ç
# Aparece Go y PHP
print(lenguajes[:3])
#Si no esta el numero lo toma como si estubiera tomando desde le primer elemento de la lsita
