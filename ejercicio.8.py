# Validar el estado de una variable después de una operación

def operacion_modifica_variable():
    variable = 10
    
    variable *= 2
    
    assert variable == 20, "La variable no tiene el estado esperado después de la operación."


operacion_modifica_variable()

print("La variable tiene el estado esperado después de la operación.")




