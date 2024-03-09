"""
EJERCICIO 8:  GESTIONAR ASERCIONES

Validar el estado de una variable después de una operación

"""


def operacion_modifica_variable():                                                                 # se define una función que no toma argumentos
    variable = 10                                                                                  # se crea una variable con un valor inicial de 10
    variable *= 2                                                                                  # luego se multiplica este valor por 2, actualizando así el valor de la variable
    assert variable == 20, "La variable no tiene el estado esperado después de la operación."      # se utiliza una asercion para verificar si la variable tiene el estado esperado luego de la operacion realizada

operacion_modifica_variable()                                                                      # se llama a la función para verificar la operacion
 
print("La variable tiene el estado esperado después de la operación.")                             # este mensaje se imprimirá solo si la aserción pasa sin errores



"""
LA IMPRESIÓN FINAL SERÁ:

La variable tiene el estado esperado después de la operación.

"""
