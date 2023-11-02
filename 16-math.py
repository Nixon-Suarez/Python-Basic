from math import * # math es un modulo el cual trae ecuaciones mas complejas

sin(x) # el seno de x.
cos(x) # el coseno de x.
tan(x) # la tangente de x.
asin(x) # el arcoseno de x.
acos(x) # el arcocoseno de x.
atan(x) # el arcotangente de x.
pi # una constante con un valor que es una aproximación de π.
radians() # una función que convierte x de grados a radianes.
degrees() # una función que convierte x de radianes a grados.
sinh() # el seno hiperbólico.
cosh() # el coseno hiperbólico.
tanh() # la tangente hiperbólico.
asinh() # el arcoseno hiperbólico.
acosh() # el arcocoseno hiperbólico.
atanh() # el arcotangente hiperbólico.
e # una constante con un valor que es una aproximación del número de Euler (e).
exp(x) # encontrar el valor de ex.
log(x) # el logaritmo natural de x.
log(x, b) # el logaritmo de x con base b.
log10(x) # el logaritmo decimal de x (más preciso que log(x, 10)).
log2(x) # el logaritmo binario de x (más preciso que log(x, 2)).
pow(x, y) # encuentra el valor de xy (toma en cuenta los dominios).
ceil(x) # devuelve el entero más pequeño mayor o igual que x.
floor(x) # el entero más grande menor o igual que x.
trunc(x) # el valor de x truncado a un entero (ten cuidado, no es equivalente a ceil o floor).
factorial(x) # devuelve x! (x tiene que ser un valor entero y no negativo).
hypot(x, y) # devuelve la longitud de la hipotenusa de un triángulo rectángulo con las longitudes de los catetos iguales a (x) y (y) (lo mismo que sqrt(pow(x, 2) + pow(y, 2)) pero más preciso).

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))