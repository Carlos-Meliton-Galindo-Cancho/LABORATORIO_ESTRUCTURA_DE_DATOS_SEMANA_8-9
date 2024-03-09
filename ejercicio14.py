"""
EJERCICIO 14:  LISTA ENLAZADA SIMPLE

Crea una función que elimine los nodos duplicados de una lista enlazada simple

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

    def eliminar_duplicados(self):
        valores_vistos = set()                                      # se inicializa un conjunto para mantener un registro de los valores de los nodos que ya se han visto
        actual = self.inicio                                        # se establecen dos punteros, actual y anterior, para recorrer la lista
        anterior = None     

        while actual:                                               # se recorre la lista mientras actual no sea None
            if actual.dato in valores_vistos:                       # en cada iteración, se verifica si el valor del nodo actual (actual.dato) ya está en el conjunto 
                anterior.siguiente = actual.siguiente               # si es un nodo duplicado, el nodo anterior (anterior) se enlaza con el nodo siguiente al nodo actual (actual.siguiente), saltándose así el nodo actual
            else:
                valores_vistos.add(actual.dato)                     # si no es un nodo duplicado, se agrega el valor del nodo actual al conjunto      
                anterior = actual                                   # y se actualiza anterior al nodo actual
            actual = actual.siguiente

lista = ListaEnlazadaSimple()                                       # se crea una instancia de ListaEnlazadaSimple llamada lista

lista.insertar_al_principio(3)
lista.insertar_al_principio(2)
lista.insertar_al_principio(3)                                      # se insertan cinco nodos en la lista 
lista.insertar_al_principio(1)
lista.insertar_al_principio(2)

print("Lista antes de eliminar duplicados:")
actual=lista.inicio
while actual:
    print(actual.dato, end=" -> ")                                  # se imprime la lista antes de eliminar los duplicados
    actual=actual.siguiente

lista.eliminar_duplicados()

print("\nLista después de eliminar duplicados:")
actual=lista.inicio
while actual:                                                       # se imprime la lista despues de eliminar los duplicados
    print(actual.dato, end=" -> ")
    actual=actual.siguiente



"""
LA IMPRESIÓN FINAL SERÁ:

Lista antes de eliminar duplicados:
2 -> 1 -> 3 -> 2 -> 3 -> 
Lista después de eliminar duplicados:
2 -> 1 -> 3 ->

"""



