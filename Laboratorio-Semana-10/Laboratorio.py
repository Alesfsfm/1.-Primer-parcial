#Ejercicio 1
# import string
# Texto = input("Ingrese un texto:\n")
# Texto_limpio = Texto.translate(str.maketrans('', '', string.punctuation)).lower()
# palabras_totales = Texto_limpio.split()
# contador = 0
# for i in palabras_totales:
#     contador+=1
# print(f"El numero de palabras totales son {contador} y las palabras son: {palabras_totales}\n")
# palabras_unicas = set(palabras_totales)
# contador1 = 0
# for i in palabras_unicas:
#     contador1+=1
# print(f"El numero de palabras unicas son {contador1} y las palabras son: {palabras_unicas}")

# diccionario = {}
# for palabras_totales in palabras_totales:
#     if palabras_totales in diccionario:
#         diccionario[palabras_totales] +=1
#     else:
#         diccionario[palabras_totales] = 1
# for palabras_totales in diccionario:
#     frecuencia = diccionario[palabras_totales]
#     print(f"La palabra '{palabras_totales}' tiene una frecuencia de'{frecuencia}' veces")
# mayor = 0
# for palabras_totales in diccionario:
#     if diccionario[palabras_totales] > mayor:
#         mayor = diccionario[palabras_totales]
#         palabra = palabras_totales
# print(f"La palabra con mayor frecuencia es:'{palabra}' y su frecuencia fue de: '{mayor}' veces.\n")  

#Ejercicio 2
# def menu():
#     ListaProductos = []

#     while True:
#         print("\n1- Registrar productos")
#         print("2- Eliminar productos")
#         print("3- Buscar productos")
#         print("4- Mostrar precios")
#         print("5- Salir")

#         Eleccion = input("Seleccione una opción: ")

#         if Eleccion == '1':
#             producto = {
#                 "Nombre": input("Ingrese el nombre del producto: "),
#                 "Categoria": input("Ingrese la categoría del producto: "),
#                 "Precio": float(input("Ingrese el precio del producto: ")),
#                 "Cantidad": int(input("Ingrese la cantidad del producto: "))
#             }
#             ListaProductos.append(producto)
#             print("Producto registrado.")

#         elif Eleccion == '2':
#             nombre = input("Ingrese el nombre del producto a eliminar: ")
#             ListaProductos = [i for i in ListaProductos if i['Nombre'].lower() != nombre.lower()]
#             print("Producto eliminado.")

#         elif Eleccion == '3':
#             nombre = input("Ingrese el nombre del producto a buscar: ")
#             for i in ListaProductos:
#                 if i['Nombre'].lower() == nombre.lower():
#                     print(i)
#                     break
#             else:
#                 print("Producto no encontrado.")

#         elif Eleccion == '4':
#             for i in sorted(ListaProductos, key=lambda x: x['Precio']):
#                 print(f"Nombre: {i['Nombre']}, Precio: {i['Precio']}, Cantidad: {i['Cantidad']}")

#         elif Eleccion == '5':
#             print("Saliendo del programa...")
#             break

#         else:
#             print("Opción inválida. Intente nuevamente.")

# menu()

#Ejercicio 3
# def menu():
#     agenda = []

#     while True:
#         print("1. Agregar contacto")
#         print("2. Buscar contacto por nombre")
#         print("3. Listar contactos en orden alfabético")
#         print("4. Salir")

#         opcion = input()

#         if opcion == '1':
#             nombre = input("Ingrese el nombre: ")
#             numero = input("Ingrese el número: ")
#             correo = input("Ingrese el correo: ")
#             contacto = (nombre, numero, correo)
#             agenda.append(contacto)
#             print("Contacto agregado correctamente. \n ", agenda)

#         elif opcion == '2': 
#             nombre_buscar = input("Ingrese el nombre a buscar: ")
#             encontrados = [i for i in agenda if i[0].lower() == nombre_buscar.lower()]
            
#             if encontrados:
#                 for i in encontrados:
#                     print(f"Nombre: {i[0]}, Número: {i[1]}, Correo: {i[2]}")
#             else:
#                 print("Contacto no encontrado.")

#         elif opcion == '3':
#             for i in sorted(agenda, key=lambda x: x[0].lower()):
#                 print(f"Nombre: {i[0]}, Número: {i[1]}, Correo: {i[2]}")

#         elif opcion == '4':
#             print("Saliendo del programa...")
#             break
#         else:
#             print("Opción inválida. Intente nuevamente.")

# menu()

#Problema 4
# import math

# def calcular_estadisticas(*args):
    
#     promedio = (lambda nums: sum(nums) / len(nums))(args)

#     datos_ordenados = sorted(args)
#     n = len(datos_ordenados)
#     if n % 2 == 0:
#         mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
#     else:
#         mediana = datos_ordenados[n//2]

#     varianza = sum((x - promedio) ** 2 for x in args) / len(args)
#     desviacion_estandar = math.sqrt(varianza)

#     return promedio, mediana, desviacion_estandar

# def menu():
#     try:
#         numeros = list(map(float, input("Ingrese una lista de números separados por espacio: ").split()))
#         promedio, mediana, desviacion_estandar = calcular_estadisticas(*numeros)
#         print(f"Promedio: {promedio:.2f}")
#         print(f"Mediana: {mediana:.2f}")
#         print(f"Desviación Estándar: {desviacion_estandar:.2f}")
#     except ValueError:
#         print("Por favor, ingrese solo números válidos.")

# menu()

#Problema 5
# import conversor

# km = float(input("Ingrese los kilómetros: "))
# celsius = float(input("Ingrese la temperatura en Celsius: "))
# litros = float(input("Ingrese los litros: "))

# print(f"{km} km = {conversor.kilometros_a_millas(km):.2f} millas")
# print(f"{celsius}°C = {conversor.celsius_a_fahrenheit(celsius):.2f}°F")
# print(f"{litros} L = {conversor.litros_a_galones(litros):.2f} galones")

#Problema 6

# class Vehiculo:
#     def __init__(self, marca, modelo, anio, precio):
#         self.marca = marca
#         self.modelo = modelo
#         self.anio = anio
#         self.precio = precio
    
#     def mostrar_informacion(self):
#         return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Precio: ${self.precio}"

# class Automovil(Vehiculo):
#     def __init__(self, marca, modelo, anio, precio, numero_puertas):
#         super().__init__(marca, modelo, anio, precio)
#         self.numero_puertas = numero_puertas

#     def mostrar_informacion(self):
#         return super().mostrar_informacion() + f", Puertas: {self.numero_puertas}"

# class Motocicleta(Vehiculo):
#     def __init__(self, marca, modelo, anio, precio, cilindrada):
#         super().__init__(marca, modelo, anio, precio)
#         self.cilindrada = cilindrada

#     def mostrar_informacion(self):
#         return super().mostrar_informacion() + f", Cilindrada: {self.cilindrada}cc"

# auto = Automovil("Toyota", "Corolla", 2023, 25000, 4)
# moto = Motocicleta("Honda", "CBR500R", 2022, 7000, 500)

# print(auto.mostrar_informacion())
# print(moto.mostrar_informacion())

#Problema 7
# import numpy as np

# lista = np.random.randint(0, 100, 50)
# print("Lista original:", lista)

# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivote = arr[0]
#         menores = [i for i in arr[1:] if i <= pivote]
#         mayores = [i for i in arr[1:] if i > pivote]
#         return quicksort(menores) + [pivote] + quicksort(mayores)

# lista = quicksort(lista)
# print("Lista ordenada:", list(map(int, lista)))

# Y = 0
# Z = len(lista) - 1
# num = int(input("Ingrese el número a encontrar:\n"))

# def busqueda_binaria(Y, Z, num):
#     while Y <= Z:
#         prom = (Y + Z) // 2
#         if lista[prom] == num:
#             return prom
#         elif num < lista[prom]:
#             Z = prom - 1
#         else:
#             Y = prom + 1
#     return -1  

# resultado = busqueda_binaria(Y, Z, num)
# if resultado != -1:
#     print(f"El número {num} fue encontrado en la posición {resultado}.")
# else:
#     print(f"El número {num} no fue encontrado en la lista.")

#Problema 8

# def merge(arr1, arr2):
#     result= []
#     i, j = 0, 0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             result.append(arr1[i])
#             i+= 1
#         else:
#             result.append(arr2[j])
#             j+=1
#     if i == len(arr1):
#         for k in range(j, len(arr2)):
#             result.append(arr2[k])
#     elif j == len(arr2):
#         for k in range(i,len(arr1)):
#             result.append(arr1[k])
#     return result

# def merge_sort(arr):
#     if len(arr)<2:
#         return arr
#     else:
#         mid = (len(arr))//2
#         arr1 = merge_sort(arr[:mid])
#         arr2 = merge_sort(arr[mid:])
#     return merge(arr1, arr2)

# lista = list(map(float, input("Ingrese una lista de números separados por espacio: ").split()))

# lista_ordenada = merge_sort(lista)
# print("Su lista original es:", lista, "\n")
# print("\nSu lista ordenada es:", lista_ordenada)

#Problema 9
lista = [1,2,5,4,3,2]
lista.sort()
print(lista)






        


        









