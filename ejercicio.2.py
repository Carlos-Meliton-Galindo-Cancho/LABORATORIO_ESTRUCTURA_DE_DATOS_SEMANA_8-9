"""
EJERCICIO 2:  GESTIONAR ASERCIONES

Verificar el tipo de dato de una variable

"""


def verificar_tipo(variable, tipo_de_dato):                                                                  # se define una función que toma dos argumentos: variable y tipo_de_dato
    assert isinstance(variable, tipo_de_dato), f"La variable no es de tipo {tipo_de_dato.__name__}."         # se utiliza una aserción para verificar si la variable es una instancia del tipo_de_dato especificado utilizando la función isinstance(). Si la variable no es del tipo especificado, se genera un AssertionError con un mensaje que indica el tipo de dato esperado

variable = 42                                                                                                # se define una variable con el valor 42
verificar_tipo(variable, int)                                                                                # se llama a la función con la variable y el tipo de dato (int) como argumentos
print("La variable es de tipo entero.")                                                                      # si la variable es del tipo entero, la aserción pasará sin problemas y se imprimirá "La variable es de tipo entero.". Si la variable no es del tipo entero, se generará un AssertionError con el mensaje correspondiente



"""
LA IMPRESIÓN FINAL SERÁ:

La variable es de tipo entero.

"""






