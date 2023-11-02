import math #Si deseas importar un módulo como un todo, puedes hacerlo usando la sentencia import nombre_del_módulo. 
import math, sys #Puedes importar más de un módulo a la vez utilizando una lista separada por comas 
import math # o repitiendo la clausula 
import sys

import math as my_module # Puede cambiar el nombre de la entidad importada "sobre la marcha" utilizando la frase as del import
result = my_module.my_function(my_module.my_data) # Si desea acceder a cualquiera de sus entidades, debes anteponer el nombre de la entidad empleando la notación con punto.


from math import pi, sqrt #from: se utiliza cuando se especifica que solo debe traer las entidades nombradas en este caso pi y sqrt
#en mis palabras: de math traeme la entidad pi y sqrt
result = sqrt(pi)
print("La raiz cuadrada del valor de PI es", result) # output da la raiz cuadrada de pi 

from math import * # *: te permite importar todas las entidades ofrecidas por un módulo
#!la variante de esta importación no se recomienda debido a la amenaza de un conflicto de nombres es aún más peligrosa aquí.





