import math

def calcular_estadisticas(*args):
    
    promedio = (lambda nums: sum(nums) / len(nums))(args)

    datos_ordenados = sorted(args)
    n = len(datos_ordenados)
    if n % 2 == 0:
        mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    else:
        mediana = datos_ordenados[n//2]

    varianza = sum((x - promedio) ** 2 for x in args) / len(args)
    desviacion_estandar = math.sqrt(varianza)

    return promedio, mediana, desviacion_estandar

def menu():
    try:
        numeros = list(map(float, input("Ingrese una lista de números separados por espacio: ").split()))
        promedio, mediana, desviacion_estandar = calcular_estadisticas(*numeros)
        print(f"Promedio: {promedio:.2f}")
        print(f"Mediana: {mediana:.2f}")
        print(f"Desviación Estándar: {desviacion_estandar:.2f}")
    except ValueError:
        print("Por favor, ingrese solo números válidos.")