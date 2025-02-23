#28.Simular una cuenta bancaria con depositos y retiros.
def menu(saldo1):
    print("\nOpciones:")
    print("a) Depositar")
    print("b) Retirar")
    print("c) Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == 'a':  
        deposito = float(input("Ingrese la cantidad de dinero a depositar: "))
        saldo1 += deposito
        print(f"Nuevo saldo: {saldo1}")
        menu(saldo1)  
    
    elif opcion == 'b':  
        retiro = float(input("Ingrese la cantidad de dinero a retirar: "))
        if retiro > saldo1:
            print("No tiene el saldo suficiente para retirar")
        else:
            saldo1 -= retiro
            print(f"Nuevo saldo: {saldo1}")
        menu(saldo1) 
    
    elif opcion == 'c':  
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Intente de nuevo.")
        menu(saldo1)  

# Inicialización
saldo = float(input("Ingrese su saldo inicial: "))
menu(saldo)  
