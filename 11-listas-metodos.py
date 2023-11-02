lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"]
lenguajes.insert(3, "Go") # insert: se agrega un elemento en el indice indicado 
lenguajes.insert(0, "C")
lenguajes.remove("Ruby") # remove: elimina elementos 
print("PHP" in lenguajes) # in buscar si algo esta dentro del listado el resultado se da en Booleano
#*lenguajes.clear() 
# limpia el listado y deja sin ningun elemento
print(len(lenguajes))
# len: Cuantos elementos contiene un listado en numeros 


