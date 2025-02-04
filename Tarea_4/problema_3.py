#3. Calcular el factorial de un numero dado.
numerofact = int(input("ingrese un numero entero cualesquiera:\n"))#int es para declarar numeros enteros
i=numerofact #sea i una variable que se va restando de 1 en 1, al mismo tiempo que multiplica el numero ingersado por el usuario para calcular el factorial
while i > 1: 
        numerofact = (i - 1) * numerofact
        i -= 1 #esto significa que i se va restando de uno en uno y se guarda en la base de datos
print("El resultado fue:", numerofact)
    

        
        

