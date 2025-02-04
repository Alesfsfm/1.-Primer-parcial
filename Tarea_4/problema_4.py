#4. Generar la secuencia de Fibonacci hasta un numero dado de terminos.
numprevio = -1
i = 1
limite = int(input("ingrese la cantidad de terminos hasta donde quiera que llegue la secuencia:"))
while limite >= 1: #0 1 1 2 3 5 8, 
    secuencia = numprevio + i
    print("la secuencia es:",secuencia)
    numprevio = i
    i = secuencia
    limite -= 1

    



    
