"""
EJERCICIO 15:  LISTA ENLAZADA SIMPLE

Implementa una función que invierta el orden de una lista enlazada simple.

"""


class Nodo:                                                   # se define la clase Nodo, que representa un nodo en la lista enlazada
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaSimple:                                    # se define la clase ListaEnlazadaSimple, que representa la lista enlazada
    def __init__(self):
        self.inicio = None

    def insertar_al_principio(self, dato):                    # se define el método insertar_al_principio
        nuevo_nodo = Nodo(dato)                               # que permite insertar un nuevo nodo al principio de la lista
        nuevo_nodo.siguiente = self.inicio
        self.inicio = nuevo_nodo

    def invertir(self):                                       #  invierte el orden de la lista enlazada
        anterior = None                                        
        actual = self.inicio                                   

        while actual:                                    
            siguiente = actual.siguiente                      # utiliza tres punteros (anterior, actual, siguiente)
            actual.siguiente = anterior                       # para recorrer la lista y cambiar los enlaces entre los nodos
            anterior = actual
            actual = siguiente

        self.inicio = anterior

    def imprimir(self):
        actual = self.inicio                                  # el método imprimir imprime los elementos de la lista enlazada
        while actual:                                         # para verificar el resultado después de la inversión
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

lista = ListaEnlazadaSimple()                                 # se crea una instancia de ListaEnlazadaSimple llamada lista

lista.insertar_al_principio(3)
lista.insertar_al_principio(2)                                # se insertan tres nodos en la lista
lista.insertar_al_principio(1)

print("Lista original:")
lista.imprimir()                                              # imprime la lista antes de invertir

lista.invertir()

print("Lista invertida:")                                     # imprime la lista despues de invertir
lista.imprimir()



"""
LA IMPRESIÓN FINAL SERÁ:

Lista original:
1 -> 2 -> 3 -> None
Lista invertida:
3 -> 2 -> 1 -> None

"""

