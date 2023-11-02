
#* El método capitalize()
# crea una nueva cadena con los caracteres tomados de la cadena fuente, pero intenta modificarlos de la siguiente manera:
# Si el primer carácter dentro de la cadena es una letra se convierte a mayúscula.
# Todas las letras restantes de la cadena se convertirán a minúsculas.

print('aBcD'.capitalize())
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

#* Metodo Center 
# La función center() justifica un texto centralizado con relleno de caracteres específicos.
print('[' + 'alpha'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
print('[' + 'gamma'.center(20, '*') + ']')

#*  El método endswith()
#El método endswith() comprueba si la cadena dada termina con el argumento especificado 
#  devuelve True(verdadero) o False(falso), dependiendo del resultado.

if "epsilon".endswith("on"):
    print("si")
else:
    print("no")

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

#*El método startswith()
#comprueba si una cadena dada comienza con la subcadena especificada.
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()

#*El método find()
#busca una subcadena y devuelve el índice de la primera aparición de esta subcadena
#no genera un error para un argumento que contiene una subcadena inexistente (devuelve -1 en dicho caso).

print("Eta".find("ta"))
print("Eta".find("mma"))
t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

#Si deseas realizar la búsqueda, no desde el principio de la cadena, sino desde cualquier posición, puedes usar una variante de dos parámetros del método find(). 
print('kappa'.find('a', 2))
#                       ☝️El segundo argumento especifica el índice en el que se iniciará la búsqueda

# Existe también una mutación de tres parámetros del método find() - el tercer argumento apunta al primer índice que no se tendrá en cuenta durante la búsqueda 
print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

#* El método isalnum()
#isalnum() comprueba si la cadena contiene solo dígitos o caracteres alfabéticos (letras) y devuelve True(verdadero) o False(falso)
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
t = 'Six lambdas'
print(t.isalnum())
t = 'ΑβΓδ'
print(t.isalnum())
t = '20E1'
print(t.isalnum())
#cualquier elemento de cadena que no sea un dígito o una letra hace que el método regrese False(falso)
#espacios tambien hace qeu de false

#* El método isalpha()
# se interesa en letras solamente
print("Moooo".isalpha())
print('Mu40'.isalpha())

#* El método isdigit()
# busca solo dígitos
print('2018'.isdigit())
print("Year2019".isdigit())

#* El método islower()
# Devuelve True si todos los caracteres son minúsculas
print("Moooo".islower())
print('moooo'.islower())

#* El método isspace()
# Devuelve True si todos los carácteres son espacio (incluyendo tabulaciones y saltos de línea).
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

#* El método isupper()
# Devuelve True si todos los caracteres son mayúsculas
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

#* El método join()
# Se utiliza para concatenar cadenas
# la cadena desde la que se ha invocado el método será utilizada como separador, puesta entre las cadenas.
print(",".join(["omicron", "pi", "rho"]))

#* El método lower()
# genera una copia de una cadena, reemplaza todas las letras mayúsculas con sus equivalentes en minúsculas
print("SiGmA=60".lower())

#* El método replace()
# Reemplaza una subcadena por otra
#                                     ⬇️Este argumento es remplazado por
print("CISCO CICLO DE VIDA".replace("CISCO",""))
#                                           ☝️Este otro
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))

#replace() con tres parámetros emplea un tercer argumento (un número) para limitar el número de reemplazos.
#                            ⬇️Este es remplazado por el primer argumento (1) oasea por si mismo "is2
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))
#                            ☝️ Este parametro es remplazado por el segundo(2) parametro en este caso "are"

#* El método rfind()
# comienzan sus búsquedas desde el final de la cadena
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

#* El método lstrip()
# devuelve una cadena recién creada formada a partir de la original eliminando todos los espacios en blanco iniciales.
print("[" + " tau ".lstrip() + "]")
print("www.cisco.com".lstrip("w."))

#* El método rstrip()
# Dos variantes del método rstrip() hacen casi lo mismo que el método lstrip, pero afecta el lado opuesto de la cadena.
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

#* El método strip()
#  crea una nueva cadena que carece de todos los espacios en blanco iniciales y finales.
print("[" + "   aleph   ".strip() + "]")

#* El método split()
# divide la cadena y crea una lista de todas las subcadenas detectadas.
# asume que las subcadenas están delimitadas por espacios en blanco
print("phi       chi\npsi".split())

#* El método swapcase()
# crea una nueva cadena intercambiando todas las letras por mayúsculas o minúsculas dentro de la cadena original
#  los caracteres en mayúscula se convierten en minúsculas y viceversa.
print("Yo sé que no sé nada.".swapcase())
print()

#* El método title()
# cambia la primera letra de cada palabra a mayúsculas, convirtiendo todas las demás a minúsculas.
print("Yo sé que no sé nada. Part 1.".title())

#* El método upper()
#  hace una copia de la cadena de origen, reemplaza todas las letras minúsculas con sus equivalentes en mayúsculas
print("Yo sé que no sé nada. Part 2.".upper())

#? capitalize(): cambia todas las letras de la cadena a mayúsculas.
#? center(): centra la cadena dentro de una longitud conocida.
#? count(): cuenta las ocurrencias de un carácter dado.
#? join(): une todos los elementos de una tupla/lista en una cadena.
#? lower(): convierte todas las letras de la cadena en minúsculas.
#? lstrip(): elimina los caracteres en blanco al principio de la cadena.
#? replace(): reemplaza una subcadena dada con otra.
#? rfind(): encuentra una subcadena comenzando por el final de la cadena.
#? rstrip(): elimina los caracteres en blanco al final de la cadena.
#? split(): divide la cadena en una subcadena usando un delimitador dado.
#? strip(): elimina los espacios en blanco iniciales y finales.
#? swapcase(): intercambia las mayúsculas y minúsculas de las letras.
#? title(): hace que la primera letra de cada palabra sea mayúscula.
#? upper(): convierte todas las letras de la cadena en letras mayúsculas.
#? endswith(): ¿La cadena termina con una subcadena determinada?
#? isalnum(): ¿La cadena consta solo de letras y dígitos?
#? isalpha(): ¿La cadena consta solo de letras?
#? islower(): ¿La cadena consta solo de letras minúsculas?
#? isspace(): ¿La cadena consta solo de espacios en blanco?
#? isupper(): ¿La cadena consta solo de letras mayúsculas?
#? startswith(): ¿La cadena consta solo de letras mayúsculas?



