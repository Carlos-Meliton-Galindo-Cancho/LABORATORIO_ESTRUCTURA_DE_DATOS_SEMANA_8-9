"""
EJERCICIO 13:  LISTA ENLAZADA SIMPLE

Implementa una función que concatene dos listas enlazadas simples.

"""


class Nodo:                                                        # se define la clase Nodo, que representa un nodo en la lista enlazada
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaSimple:                                         # se define la clase ListaEnlazadaSimple, que representa la lista enlazada
    def __init__(self):
        self.inicio = None

    def insertar_al_principio(self, dato):                         # se define el método insertar_al_principio
        nuevo_nodo = Nodo(dato)                                    # que permite insertar un nuevo nodo al principio de la lista
        nuevo_nodo.siguiente = self.inicio
        self.inicio = nuevo_nodo

    def concatenar(self, otra_lista):                              
        if self.inicio is None:
            self.inicio = otra_lista.inicio                        # es un método que toma como argumento otra lista enlazada (otra_lista) y la concatena a la lista actual
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = otra_lista.inicio

    def imprimir(self):
        actual = self.inicio                                       # método que imprime todos los nodos de la lista enlazada
        while actual:                                              # comienza desde el primer nodo y avanza a traves de la lista
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

lista1 = ListaEnlazadaSimple()                                     # se crea una instancia de ListaEnlazadaSimple llamada lista
lista1.insertar_al_principio(3)
lista1.insertar_al_principio(2)                                    # se insertan tres nodos a la primera lista 
lista1.insertar_al_principio(1)

lista2 = ListaEnlazadaSimple()
lista2.insertar_al_principio(6)
lista2.insertar_al_principio(5)                                    # se insertan tres nodos a la segunda lista 
lista2.insertar_al_principio(4)

print("Lista 1:")
lista1.imprimir()
print("Lista 2:")
lista2.imprimir()

lista1.concatenar(lista2)                                          # se concatena lista2 a lista1 usando el método (concatenar)
print("Lista concatenada:")                                        
lista1.imprimir()                                                  # finalmente se imprime la lista concatenada para verificar el resultado



"""
LA IMPRESIÓN FINAL SERÁ:

Lista 1:
1 -> 2 -> 3 -> None
Lista 2:
4 -> 5 -> 6 -> None
Lista concatenada:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

"""





