"""
EJERCICIO 6:  GESTIONAR ASERCIONES

Asegurar que un ciclo while se ejecuta al menos una vez.

"""


def validar_ciclo_while():
    contador=8                                                                    # se inicializa la variable contador con el valor 8
    while contador < 10:                                                          # se inicia un bucle while que se ejecutará mientras el valor de contador sea menor que 10
        if contador==9:                                                           # se verifica si el valor del contador es igual a 9
            print("el ciclo while se ejecuto al menos una vez")                   # si es así, se imprime un mensaje indicando que el ciclo while se ejecutó al menos una vez 
            break                                                                 # y se rompe el bucle utilizando la instrucción break
        contador += 1
        print("el ciclo while se ejecuto al menos una vez")                       # se incrementa el valor del contador en cada iteración del bucle y se imprime un mensaje indicando que el ciclo while se ejecutó al menos una vez
            
    assert contador < 10, "el ciclo while no se ejecuto al menos una vez"         # se coloca una aserción que verifica si el valor del contador es menor que 10. Si esta aserción falla, se levanta una excepción con el mensaje "el ciclo while no se ejecutó al menos una vez"
   
validar_ciclo_while()                                                             # finalmente se llama a la función validar_ciclo_while para ejecutarla y realizar las verificaciones


        
"""
LA IMPRESIÓN FINAL SERÁ:

el ciclo while se ejecuto al menos una vez

"""




