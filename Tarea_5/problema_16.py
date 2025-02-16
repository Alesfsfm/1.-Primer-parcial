#16. Contar el numero de vocales y consonantes de una cadena
vocales = "aeiou"
contador_vocales = 0
consonantes = "bcdfghjklmnpqrstvwxyz"
contador_consonantes = 0
cadena = str(input("ingrese palabras, letras, o frases\n"))
for letra in cadena:
    if letra.lower() in vocales:
        contador_vocales += 1
    elif letra.lower() in consonantes:
        contador_consonantes +=1

print("el numero de vocales es:", contador_vocales)
print("el numero de consonantes es:", contador_consonantes)
        

