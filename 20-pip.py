
#! Esto se debe ejecutar en la terminal de tu computadora

# Ahora estamos listos para preguntarle a pip qué puede hacer por nosotros. Hagámoslo, emite el siguiente comando:
#* pip help

# Si deseas saber más sobre cualquiera de las operaciones enumeradas, puedes utilizar la siguiente forma de invocación de pip:
#* pip help (operación o comando)
# ejemplo:
#* pip help install 
# te mostrará información detallada sobre el uso y la parametrización del comando install.

# para  brindarte más información sobre cualquiera de los paquetes instalados 

#* pip show nombre_del_paquete
# ejemplo:
#* pip show pip

# buscar en PyPI para encontrar el paquete deseado. Este tipo de búsqueda se inicia con el siguiente comando:
#* pip search anystring
# La cadena anystring que se proporciono será buscada en:
# Los nombres de todos los paquetes.
# Las cadenas de resumen de todos los paquetes.



#* vamos a instalar un paquete llamado pygame:
# es una biblioteca extendida y compleja que permite a los programadores desarrollar juegos de computadora usando Python.

# Si eres administrador del sistema, puedes instalar pygame usando el siguiente comando:
#* pip install pygame

# Si no eres un administrador, o no quieres engordar tu sistema operativo instalando pygame en todo el sistema, puedes instalarlo solo para ti:
#* pip install --user pygame


# Depende de ti cuál de los procedimientos anteriores deseas que se lleve a cabo.
#* pip install --user pygame

# Te alentamos a usar:
#* pip show pygame y pip list
# para obtener más información sobre lo que realmente sucedió.

#* El comando pip install tiene dos habilidades adicionales importantes:

# Es capaz de actualizar un paquete instalado localmente; por ejemplo, si deseas asegurarte de que estás utilizando la última versión de un paquete en particular, puedes ejecutar el siguiente comando:

#* pip install -U nombre_del_paquete
#             ☝️-U significa actualizar

# instalar una versión seleccionada por el usuario
#* pip install nombre_del_paquete==versión_del_paquete
# ejempo:
#* pip install pygame==1.9.2

# Si alguno de los paquetes instalados actualmente ya no es necesario y deseas deshacerte de el, pip también será útil. Su comando uninstall ejecutará todos los pasos necesarios.
# a sintaxis requerida es clara y simple:
#* pip uninstall nombre_del_paquete


# Así que si ya no quieres pygame, puedes ejecutar el siguiente comando:
#! pip uninstall pygame

#! La lista de las actividades principales de pip tiene el siguiente aspecto:

#? pip help operación_o_comando â muestra una breve descripción de pip.
#? pip list â muestra una lista de los paquetes instalados actualmente.
#? pip show nombre_del_paquete â muestra información que incluyen las dependencias del paquete.
#? pip search cadena â busca en los directorios de PyPI para encontrar paquetes cuyos nombres contengan cadena.
#? pip install nombre â instala el paquete nombre en todo el sistema (espera problemas cuando no tengas privilegios de administrador).
#? pip install --user nombre â instala nombre solo para ti; ningún otro usuario de la plataforma podrá utilizarlo.
#? pip install -U nombre â actualiza un paquete previamente instalado.
#? pip uninstall nombre â desinstala un paquete previamente instalado.