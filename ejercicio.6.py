# Asegurar que un ciclo while se ejecuta al menos una vez.

def validar_ciclo_while():
    contador=8
    while contador < 10:
        if contador==9:
            print("el ciclo while se ejecuto al menos una vez")
            break
        contador += 1
        print("el ciclo while se ejecuto al menos una vez")
        
        
    assert contador < 10, "el ciclo while no se ejecuto al menos una vez"
   

validar_ciclo_while()



............
        












