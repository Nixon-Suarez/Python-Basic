texto = "Hola Mundo"
        #0123456789        
print(texto)
print(texto.upper()) #Mayusculas  
print(texto.lower()) #Minusculas  
print(texto.find("Mun")) #Buscar una cadena de texto dentro del string (Me da el indice)
print(texto.replace("Mundo", "Hola")) #Reemplazar una cadena de texto por otra  

nuevoTexto = texto.replace("Mundo", "Hola")
print (nuevoTexto, texto) # le damos una variable 
print("Mundo" in texto) #tambien busca una cadena de texto dentro del string pero nos da un Booleano (true o flase)


