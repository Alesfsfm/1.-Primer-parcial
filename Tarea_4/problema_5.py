#5. Verificar si un numero es primo.
numero = int(input("Ingrese un numero:"))
if numero % 2 == 0 or numero % 3 == 0: #el operador % te da el residuo como resultado, y si el residuo entre 2 o 3 es igual a cero, el numero NO es primo
    print("su numero NO es primo")#if es un condicional
else: print("su numero ES primo") #else se activa cuando la primera condicion no se cumple





