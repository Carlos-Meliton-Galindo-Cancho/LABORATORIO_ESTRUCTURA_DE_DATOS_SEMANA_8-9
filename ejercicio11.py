"""
EJERCICIO 11:  LISTA ENLAZADA SIMPLE

Implementa una función que sume todos los nodos de una lista enlazada simple

"""

class Nodo:                                                         # se define la clase Nodo, que representa un nodo en la lista enlazada
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaSimple:                                          # se define la clase ListaEnlazadaSimple, que representa la lista enlazada
    def __init__(self):
        self.inicio = None

    def insertar_al_principio(self, dato):                          # se define el método insertar_al_principio
        nuevo_nodo = Nodo(dato)                                     # que permite insertar un nuevo nodo al principio de la lista
        nuevo_nodo.siguiente = self.inicio
        self.inicio = nuevo_nodo

    def suma_nodos(self):                                           # se define el método suma_nodos
        suma = 0                                                    # que suma todos los valores de los nodos en la lista enlazada
        actual = self.inicio
        while actual:                                               # itera a través de la lista mientras acumula la suma de los valores de los nodos
            suma += actual.dato
            actual = actual.siguiente
        return suma

lista = ListaEnlazadaSimple()                                       # se crea una instancia de la lista enlazada

lista.insertar_al_principio(1)
lista.insertar_al_principio(2)                                      # se insertan algunos nodos al principio de la lista
lista.insertar_al_principio(3)

print("Suma de los nodos de la lista:", lista.suma_nodos())         # luego se llama al método suma_nodos y se imprime la suma obtenida


"""
LA IMPRESIÓN FINAL SERÁ:

Suma de los nodos de la lista: 6

"""
                                                                
