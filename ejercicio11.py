

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

    def suma_nodos(self):
        suma = 0
        actual = self.inicio
        while actual:
            suma += actual.dato
            actual = actual.siguiente
        return suma

# Ejemplo de uso
lista = ListaEnlazadaSimple()
lista.insertar_al_principio(1)
lista.insertar_al_principio(2)
lista.insertar_al_principio(3)

print("Suma de los nodos de la lista:", lista.suma_nodos())
