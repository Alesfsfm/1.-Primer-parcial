#6. Calcular el interes compuesto dado un capital, tasa y tiempo.
capital = float(input("Ingrese la cantidad de capital invertido:\n"))
tasa = float(input("Ingrese el porcentaje de tasa de interes(en terminos porcentuales):\n"))
tiempo = int(input("Ingrese la cantidad de anios:\n"))
Interescompuesto = capital*(1 + tasa)**tiempo
print("Su interes compuesto es:", Interescompuesto)
