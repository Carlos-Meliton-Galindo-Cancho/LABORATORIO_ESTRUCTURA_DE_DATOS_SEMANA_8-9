# Asegurar que una función retorna un valor específico

def funcion_a_probar():

    return 42  # Valor que debe retornar la función


resultado = funcion_a_probar()
assert resultado == 42, "La función no retornó el valor esperado."

print("La función retornó el valor esperado:", resultado)





"""
Para asegurar que una función retorne un valor específico, puedes utilizar una aserción justo después de llamar a la función.


Luego, se llama a la función y se guarda el resultado en una variable llamada resultado.
Justo después de llamar a la función, se utiliza una aserción para verificar si el resultado es igual al valor específico esperado.

"""