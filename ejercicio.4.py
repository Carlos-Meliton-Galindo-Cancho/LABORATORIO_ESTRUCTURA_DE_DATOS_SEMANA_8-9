"""
EJERCICIO 4:  GESTIONAR ASERCIONES

Asegurar que una lista no esté vacía

"""


def verificar_lista(lista):                                                     # se define una función que toma un argumento (lista)
    assert len(lista) > 0, "La lista no puede estar vacía."                     # se utiliza una aserción para verificar si la longitud de la lista es mayor que cero

mi_lista = [1, 2, 3]                                                            # se define una lista con algunos elementos
verificar_lista(mi_lista)                                                       # luego se llama a la función con esta lista como argumento. Si la lista no está vacía (su longitud es mayor que cero), la aserción no generará ningún error y el programa continuará su ejecución
print("la lista no esta vacía")                                                 # este mensaje se imprimirá solo si la aserción en la función verificar_lista pasa sin errores



"""
LA IMPRESIÓN FINAL SERÁ:

la lista no esta vacía

"""


