# print("Actividades salon    ")

# v1 = 100

# v1 -= 2

# if v1 <= 1000:
#     if v1 >= 99:
#         print("Dentro del if\n")
#         print("Aun dentro del if\n")

# print("estas fuera del if")

# nombre = input()

# print("Tu nombre es: ", nombre)


# edad = -1
# anioactual = 2025
# anionacimiento = int(input("Ingrese el year de nacimiento: \n"))

# edad = anioactual - anionacimiento

# print("tienes", edad, "anios sin baniarte")
# print("tienes %d anios sin baniarte"% edad)

#Actividad 2: hacer una calculadora
while True:
    try:
        numero1 = int(input("Ingrese un numero entero cualesquiera\n"))
        if numero1 > 0 and numero1 < 0:
            break
    except ValueError:
        print("debe de elejir un numero diferente de cero\n")

while True:
    try:
        numero2 = int(input("Ingrese otro numero entero cualesquiera\n"))
        if numero2 > 0 and numero2 < 0:
            break
    except ValueError:
        print("debe de elegir un numero diferente de cero\n")
    
print("suma =", numero1 + numero2)
print("resta =", numero1 - numero2)
print("multiplicacion=", numero1 * numero2)
print("division=", numero1 / numero2)
3

    

        
    

