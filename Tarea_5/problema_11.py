#Verificar si una cadena es palindromo
cadena = str(input("Ingrese una palabra, frase, o cifra numerica de su agrado:"))
if cadena == cadena[::-1]: #variable[::-1], invierte lo que el usuario ingreso
    print("Es palindromo.")
else:
    print("no es palindromo")
