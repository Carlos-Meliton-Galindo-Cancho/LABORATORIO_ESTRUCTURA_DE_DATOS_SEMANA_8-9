# Desarrollar el código de buscar nodo en la lista enlazada simple

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaSimpleEnlazada:
    def __init__(self):
        self.inicio = None

    def insertar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.inicio
        self.inicio = nuevo_nodo

    def buscar(self, dato):
        actual = self.inicio

        while actual:
            if actual.dato == dato:
                print(f"El dato {dato} se encuentra en la lista.")
                return True
            actual = actual.siguiente

        print(f"El dato {dato} no se encuentra en la lista.")
        return False

lista = ListaSimpleEnlazada()
lista.insertar_al_principio(1)
lista.insertar_al_principio(2)
lista.insertar_al_principio(3)

lista.buscar(2)
lista.buscar(4)


actual=lista.inicio
while actual:
    print(actual.dato, end=" -> ")
    actual=actual.siguiente
"""
actual=lista.inicio
while actual:
    if actual.siguiente is None:
        print(actual.dato)
        break
    else:
        print(actual.dato, end=" -> ")
        actual=actual.siguiente
"""




