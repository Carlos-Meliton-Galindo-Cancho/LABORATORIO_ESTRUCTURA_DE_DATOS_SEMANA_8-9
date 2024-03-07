# Asegurar que una lista no esté vacía

def verificar_lista(lista):
    assert len(lista) > 0, "La lista no puede estar vacía."

mi_lista = [1, 2, 3]
verificar_lista(mi_lista)  
print("la lista no esta vacía")

