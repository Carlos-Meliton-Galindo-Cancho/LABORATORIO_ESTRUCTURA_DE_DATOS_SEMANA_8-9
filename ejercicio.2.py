# Verificar el tipo de dato de una variable

def verificar_tipo(variable, tipo_de_dato):
    assert isinstance(variable, tipo_de_dato), f"La variable no es de tipo {tipo_de_dato.__name__}."

variable = 42
verificar_tipo(variable, int)
print("La variable es de tipo entero.")










"""

La aserción isinstance(variable, tipo) verifica si la variable es una instancia del tipo de dato especificado.


"""