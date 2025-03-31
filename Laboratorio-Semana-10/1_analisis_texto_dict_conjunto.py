
import string
Texto = input("Ingrese un texto:\n")
Texto_limpio = Texto.translate(str.maketrans('', '', string.punctuation)).lower()
palabras_totales = Texto_limpio.split()
contador = 0
for i in palabras_totales:
    contador+=1
print(f"El numero de palabras totales son {contador} y las palabras son: {palabras_totales}\n")
palabras_unicas = set(palabras_totales)
contador1 = 0
for i in palabras_unicas:
    contador1+=1
print(f"El numero de palabras unicas son {contador1} y las palabras son: {palabras_unicas}")

diccionario = {}
for palabras_totales in palabras_totales:
    if palabras_totales in diccionario:
        diccionario[palabras_totales] +=1
    else:
        diccionario[palabras_totales] = 1
for palabras_totales in diccionario:
    frecuencia = diccionario[palabras_totales]
    print(f"La palabra '{palabras_totales}' tiene una frecuencia de'{frecuencia}' veces")
mayor = 0
for palabras_totales in diccionario:
    if diccionario[palabras_totales] > mayor:
        mayor = diccionario[palabras_totales]
        palabra = palabras_totales
print(f"La palabra con mayor frecuencia es:'{palabra}' y su frecuencia fue de: '{mayor}' veces.\n")