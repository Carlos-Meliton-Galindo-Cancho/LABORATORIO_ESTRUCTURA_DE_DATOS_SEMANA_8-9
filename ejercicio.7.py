"""
EJERCICIO 7:  GESTIONAR ASERCIONES

Asegurar que una función retorna un valor específico

"""


def funcion_a_probar():                                                   # se define una función que no toma argumentos y devuelve el valor 42                          
    return 42  

resultado = funcion_a_probar()                                            # se llama a la función y se asigna su resultado a la variable (resultado)
assert resultado == 42, "La función no retornó el valor esperado."        # se utiliza una aserción para verificar si el resultado es igual a 42. Si el resultado no es igual a 42, se generará un AssertionError con el mensaje "La función no retornó el valor esperado"

print("La función retornó el valor esperado:", resultado)                 # este mensaje se imprimirá solo si la aserción pasa sin errores



"""
LA IMPRESIÓN FINAL SERÁ:

La función retornó el valor esperado: 42

"""
