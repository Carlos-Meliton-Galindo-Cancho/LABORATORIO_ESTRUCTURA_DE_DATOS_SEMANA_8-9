"""
EJERCICIO 12:  LISTA ENLAZADA SIMPLE

Crea una función que devuelva la longitud de una lista enlazada simple

"""



class Nodo:                                                      # se define la clase Nodo, que representa un nodo en la lista enlazada
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaSimple:                                       # se define la clase ListaEnlazadaSimple, que representa la lista enlazada
    def __init__(self):
        self.inicio = None

    def insertar_al_principio(self, dato):                       # se define el método insertar_al_principio
        nuevo_nodo = Nodo(dato)                                  # que permite insertar un nuevo nodo al principio de la lista
        nuevo_nodo.siguiente = self.inicio
        self.inicio = nuevo_nodo

    def longitud(self):
        contador = 0
        actual = self.inicio                                     # calcula la longitud de la lista contando la cantidad de nodos
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

lista = ListaEnlazadaSimple()                                    # se crea una instancia de ListaEnlazadaSimple llamada lista

lista.insertar_al_principio(3)
lista.insertar_al_principio(2)                                   # se insertan tres nodos en la lista 
lista.insertar_al_principio(1)

print("Longitud de la lista:", lista.longitud())                 # se imprime la longitud de la lista utilizando el método longitud()



"""
LA IMPRESIÓN FINAL SERÁ:

Longitud de la lista: 3

"""