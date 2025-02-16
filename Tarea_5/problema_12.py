#12. Encontrar el mayor entre 3 numeros dados
num1 = float(input("Ingrese un numero cualesquiera:"))
num2 = float(input("Ingrese un numero cualesquiera:"))
num3 = float(input("Ingrese un numero cualesquiera:"))
if num1 > num2 and num1 > num3:
    print("El numero mayor es:", num1)
elif num2 > num3:
    print("El numero mayor es:", num2)
else:
    print("El numero mayor es:", num3)