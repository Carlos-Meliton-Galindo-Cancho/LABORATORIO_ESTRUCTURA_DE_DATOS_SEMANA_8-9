"""
EJERCICIO 1:  GESTIONAR ASERCIONES

Validar la edad de un usuario

"""


def validar_edad():
    edad = input("Ingresa tu edad: ")                                             # se solicita al usuario que ingrese su edad mediante la función input()
    assert edad.isdigit(), "La edad debe ser un número (digitos)."                # se utiliza una aserción para verificar si la entrada de edad es un número (función isdigit()). Si la entrada no es un número, se genera un AssertionError con el mensaje "La edad debe ser un número (dígitos)"
    edad = int(edad)                                                              # después de la validación, la edad ingresada se convierte a un entero utilizando la función int()
    assert edad >= 0, "La edad debe ser un número positivo."                      # se utiliza otra aserción para asegurarse de que la edad ingresada sea un número positivo. Si la edad es menor que cero, se genera un AssertionError con el mensaje "La edad debe ser un número positivo"
    return edad

edad_usuario = validar_edad()                                                     # se llama a la función para obtener la edad válida del usuario
print("Edad válida ingresada:", edad_usuario, "años")                             # luego se imprime un mensaje indicando la edad válida ingresada por el usuario



"""
LA IMPRESIÓN FINAL SERÁ:

Ingresa tu edad: 19
Edad válida ingresada: 19 años

"""


