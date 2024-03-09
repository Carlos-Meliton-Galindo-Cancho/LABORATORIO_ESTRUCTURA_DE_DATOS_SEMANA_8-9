"""
EJERCICIO 3:  GESTIONAR ASERCIONES

Validar el rango de una calificación

"""


def validar_calificacion(calificacion):                                                               # se define una función que toma un argumento (calificacion)
    assert 0 <= calificacion <= 20, "La calificación debe estar en el rango de 0 a 20."               # se utiliza una aserción para verificar si la calificación está dentro del rango permitido (entre 0 y 20, ambos inclusive) 

calificacion = 20                                                                                     # se define una variable con el valor 20, que está dentro del rango permitido
validar_calificacion(calificacion)                                                                    # se llama a la función con esta calificación como argumento. Si la calificación está dentro del rango permitido, la aserción no generará ningún error y el programa continuará su ejecución
print("la calificacion esta dentro del rango")                                                        # este mensaje se imprimirá solo si la aserción en la función validar_calificacion pasa sin errores



"""
LA IMPRESIÓN FINAL SERÁ:

la calificacion esta dentro del rango

"""


