# Crea una función que devuelva la longitud de una lista enlazada simple

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaSimple:
    def __init__(self):
        self.inicio = None

    def insertar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.inicio
        self.inicio = nuevo_nodo

    def longitud(self):
        contador = 0
        actual = self.inicio
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

lista = ListaEnlazadaSimple()
lista.insertar_al_principio(3)
lista.insertar_al_principio(2)
lista.insertar_al_principio(1)

print("Longitud de la lista:", lista.longitud())



