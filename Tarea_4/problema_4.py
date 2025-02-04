#4. Generar la secuencia de Fibonacci hasta un numero dado de terminos.
numprevio = -1
i = 1
limite = int(input("ingrese la cantidad de terminos hasta donde quiera que llegue la secuencia:"))
while limite >= 1: #0 1 1 2 3 5 8 etc.. orden de la secuencia fibonacci
    secuencia = numprevio + i
    print("la secuencia es:",secuencia)
    numprevio = i
    i = secuencia
    limite -= 1 #el limite se va restando hasta llegar a 1, para romper el ciclo e imprimir resultados
    

    



    
