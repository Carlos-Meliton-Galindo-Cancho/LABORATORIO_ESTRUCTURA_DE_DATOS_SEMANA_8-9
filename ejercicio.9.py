

try:
    import modulo_a_importar
    modulo_importado_correctamente = True
except ImportError:
    modulo_importado_correctamente = False

assert modulo_importado_correctamente, "El módulo no se ha importado correctamente."

# Ejemplo de uso
resultado = modulo_a_importar.funcion_en_modulo()
print(resultado)


....