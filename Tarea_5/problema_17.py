#17.Implementar estructuras de datos basicas: pila, cola y lista enlazada
from collections import deque

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if self.items:
            return self.items.pop()
        return None

    def cima(self):
        if self.items:
            return self.items[-1]
        return None

class Cola:
    def __init__(self):
        self.items = deque()

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if self.items:
            return self.items.popleft()
        return None

    def frente(self):
        if self.items:
            return self.items[0]
        return None

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def agregar_inicio(self, data):
        nuevo_nodo = Nodo(data)
        nuevo_nodo.next = self.head
        self.head = nuevo_nodo

    def imprimir_lista(self):
        actual = self.head
        while actual:
            print(actual.data, end=" -> ")
            actual = actual.next
        print("None")


pila = Pila()
cola = Cola()
lista = ListaEnlazada()


pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
print(f"Cima de la pila: {pila.cima()}")  


cola.encolar(10)
cola.encolar(20)
cola.encolar(30)
print(f"Frente de la cola: {cola.frente()}")  

lista.agregar_inicio(5)
lista.agregar_inicio(10)
lista.agregar_inicio(15)
print("Lista enlazada:")
lista.imprimir_lista() 

print(f"Desapilando de la pila: {pila.desapilar()}")  
print(f"Desencolando de la cola: {cola.desencolar()}")  
