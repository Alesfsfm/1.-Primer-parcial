#9. Generar una lista de numeros pares e impares hasta un lımite dado.
i = 1
limite = int(input("Ingrese el limite de la lista:"))
while limite >= 1:
    lista = i
    if i % 2 == 0: #segun el residuo de i, la consola lo identificara como par o impar
        print(lista,"es par")
    else: print(lista,"es impar")
    i+= 1 
    limite -= 1
