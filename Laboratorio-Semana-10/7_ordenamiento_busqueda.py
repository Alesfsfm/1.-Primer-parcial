import numpy as np

lista = np.random.randint(0, 100, 50)
print("Lista original:", lista)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [i for i in arr[1:] if i <= pivote]
        mayores = [i for i in arr[1:] if i > pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)

lista = quicksort(lista)
print("Lista ordenada:", list(map(int, lista)))

Y = 0
Z = len(lista) - 1
num = int(input("Ingrese el número a encontrar:\n"))

def busqueda_binaria(Y, Z, num):
    while Y <= Z:
        prom = (Y + Z) // 2
        if lista[prom] == num:
            return prom
        elif num < lista[prom]:
            Z = prom - 1
        else:
            Y = prom + 1
    return -1  

resultado = busqueda_binaria(Y, Z, num)
if resultado != -1:
    print(f"El número {num} fue encontrado en la posición {resultado}.")
else:
    print(f"El número {num} no fue encontrado en la lista.")