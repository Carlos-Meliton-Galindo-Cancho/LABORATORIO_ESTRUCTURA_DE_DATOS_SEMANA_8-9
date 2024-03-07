# Crea una función que elimine los nodos duplicados de una lista enlazada simple

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

    def eliminar_duplicados(self):
        valores_vistos = set()
        actual = self.inicio
        anterior = None      # anterior = None: Se inicializa una variable llamada anterior que se utilizará para realizar 
                             #  el seguimiento del nodo anterior al nodo actual. Inicialmente se establece en None.

        while actual:
            if actual.dato in valores_vistos:
                
                anterior.siguiente = actual.siguiente
            else:
                valores_vistos.add(actual.dato)
                
                anterior = actual
           
            actual = actual.siguiente


lista = ListaEnlazadaSimple()
lista.insertar_al_principio(3)
lista.insertar_al_principio(2)
lista.insertar_al_principio(3)
lista.insertar_al_principio(1)
lista.insertar_al_principio(2)

print("Lista antes de eliminar duplicados:")
actual=lista.inicio
while actual:
    print(actual.dato, end=" -> ")
    actual=actual.siguiente

lista.eliminar_duplicados()

print("\nLista después de eliminar duplicados:")
actual=lista.inicio
while actual:
    print(actual.dato, end=" -> ")
    actual=actual.siguiente































