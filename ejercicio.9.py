"""
EJERCICIO 9:  GESTIONAR ASERCIONES

Asegurar que un módulo se ha importado correctamente

"""


try:
    import modulo_que_queremos_importar                               # se intenta importar el módulo que deseamos utilizando un bloque try-except
    modulo_importado = True                                           # si la importación tiene éxito, la variable modulo_importado se establece en True
except ImportError:                                                   
    modulo_importado = False                                          # si falla la importación debido a un ImportError, la variable modulo_importado se establece en False

assert modulo_importado, "Error al importar el módulo."               # se utiliza una aserción para verificar si el módulo se ha importado correctamente. Si modulo_importado es True, la aserción pasará sin problemas. Si es False, lo que indica que hubo un error al importar el módulo, se generará un AssertionError con el mensaje "Error al importar el módulo."



"""
LA IMPRESIÓN FINAL SERÁ:

AssertionError: Error al importar el módulo.

"""