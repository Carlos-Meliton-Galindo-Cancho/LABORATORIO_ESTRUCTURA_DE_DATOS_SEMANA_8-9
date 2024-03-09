"""
EJERCICIO 5:  GESTIONAR ASERCIONES

Validar la igualdad de dos objetos

"""


def validar_igualdad(objeto1, objeto2):                                   # se define una función que toma dos argumentos, objeto1 y objeto2
    assert objeto1 == objeto2, "Los objetos no son iguales."              # se utiliza una aserción para verificar si los dos objetos son iguales
    
cadena1 = "Hola"                                                          # se definen dos cadenas, cadena1 y cadena2, que contienen el mismo texto "Hola"
cadena2 = "Hola"
validar_igualdad(cadena1, cadena2)                                        # luego se llama a la función con estas dos cadenas como argumentos. Si las dos cadenas son iguales, la aserción no generará ningún error y el programa continuará su ejecución
print("los dos objetos son iguales")                                      # este mensaje se imprimirá solo si la aserción en la función validar_igualdad pasa sin errores



"""
LA IMPRESIÓN FINAL SERÁ:

los dos objetos son iguales

"""

