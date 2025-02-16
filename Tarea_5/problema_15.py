#15. Determinar si un year es bisiesto
year = int(input("Ingrese un year:"))
if year % 4 == 0:
    print("Es un year bisiesto")
else:
    print("no es un year bisiesto")