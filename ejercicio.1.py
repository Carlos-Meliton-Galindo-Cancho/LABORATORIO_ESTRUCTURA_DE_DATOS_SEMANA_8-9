# Validar la edad de un usuario

def validar_edad():
    edad = input("Ingresa tu edad: ")
    assert edad.isdigit(), "La edad debe ser un número (digitos)."
    edad = int(edad)
    assert edad >= 0, "La edad debe ser un número positivo."
    return edad

edad_usuario = validar_edad()
print("Edad válida ingresada:", edad_usuario, "años")
