print ("Me gusta ser un modulo")
print(__name__)

counter = 0 # contador funcion 1

if __name__ == "__main__": # Funcion 2
    print("Yo prefiero ser un módulo")
else:
    print("Me gusta ser un módulo")

#! Python no tiene medios para permitirte ocultar tales variables a los ojos de los usuarios del módulo.
#!puedes informar a tus usuarios que esta es tu variable, que pueden leerla, pero que no deben modificarla bajo ninguna circunstancia.Esto se hace anteponiendo al nombre de la variable _ (un guión bajo) o __ (dos guiones bajos), pero recuerda, es solo un acuerdo