"""
EJERCICIO 10:  LISTA ENLAZADA SIMPLE

Desarrollar el código de buscar nodo en la lista enlazada simple

"""



class Nodo:                                                                  # se define una clase Nodo que representa un nodo en la lista enlazada 
    def __init__(self, dato):                                                # cada nodo tiene un atributo dato que almacena el valor del nodo                                         
        self.dato = dato
        self.siguiente = None                                                # y un atributo siguiente que apunta al siguiente nodo en la lista

class ListaSimpleEnlazada:                                                   # se define una clase que representa la lista enlazada en sí
    def __init__(self):
        self.inicio = None                                                   # tiene un atributo inicio que apunta al primer nodo en la lista

    def insertar_al_principio(self, dato):                                   # se define un método insertar_al_principio que permite insertar un nuevo nodo al principio de la lista
        nuevo_nodo = Nodo(dato)                                              # crea un nuevo nodo con el dato proporcionado
        nuevo_nodo.siguiente = self.inicio                                   # lo enlaza al principio de la lista
        self.inicio = nuevo_nodo                                             # actualizando el atributo inicio para que apunte al nuevo nodo

    def buscar(self, dato):                                                  # se define un método buscar que recorre la lista enlazada para buscar un dato específico
        actual = self.inicio

        while actual:                                                        # comienza desde el primer nodo y se desplaza a través de la lista mientras busca el dato
            if actual.dato == dato:
                print(f"El dato {dato} se encuentra en la lista.")           # si encuentra el dato, imprime un mensaje indicando que el dato se encuentra en la lista y devuelve True
                return True
            actual = actual.siguiente                                        # actualiza la variable actual

        print(f"El dato {dato} no se encuentra en la lista.")                # si no encuentra el dato, imprime un mensaje indicando que el dato no se encuentra en la lista y devuelve False
        return False

lista = ListaSimpleEnlazada()                                                # se crea una instancia de la lista enlazada (lista)

lista.insertar_al_principio(1)                        
lista.insertar_al_principio(2)                                               # se insertan algunos nodos al principio de la lista
lista.insertar_al_principio(3)

lista.buscar(2)                                                              # luego se llama al método (buscar) para buscar elementos en la lista
lista.buscar(4)                                                              

actual=lista.inicio
while actual:                                                                # se realiza un bucle para imprimir todos los nodos de la lista enlazada
    print(actual.dato, end=" -> ")
    actual=actual.siguiente



"""
LA IMPRESIÓN FINAL SERÁ:

El dato 2 se encuentra en la lista.
El dato 4 no se encuentra en la lista.
3 -> 2 -> 1 ->

"""

