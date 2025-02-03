def menu():
    while True:
        try:
             print("1. suma\n")
             print("2. resta\n")
             print("3. multiplicacion\n")
             print("4. division\n")
             print("5. salir\n")
             opcion = int(input("\nIngrese un opperador o si desea salir del programa:\n"))
             if 1 <= opcion <= 5:
                 break
             print("\nIngrese un numero entre 1 y 5\n")
        except ValueError:
            print("\n Ingrese un numero valido\n")
    if opcion == 1:
        variable1 = float(input("Ingrese un numero cualesquiera:\n"))
        variable2 = float(input("Ingrese otro numero cualesquiera:\n"))
        resultado_suma = variable1 + variable2
        print("El resultado de la suma es:\n", resultado_suma)
    elif opcion == 2:
        variable1 = float(input("Ingrese un numero cualesquiera:\n"))
        variable2 = float(input("Ingrese otro numero cualesquiera\n"))
        resultado_resta = variable1 - variable2
        print("El resultado de la resta es:\n", resultado_resta)
    elif opcion == 3:
        variable1 = float(input("Ingrese un numero cualesquiera:\n"))
        variable2 = float(input("Ingrese otro numero cualesquiera\n"))
        resultado_multiplicaion = variable1 * variable2
        print("El resultado de la multiplicacion es:\n", resultado_multiplicaion)
    elif opcion == 4:
        while True:
            try:
                variable1 = float(input("Ingrese un numero cualesquiera:\n"))
                variable2 = float(input("Ingrese un numero cualesquiera:\n"))
                if variable2 < 0 or variable2 > 0:
                    break
                print("ERROR! NO PUEDES DIVIDIR ENTRE CERO!\n")
            except ZeroDivisionError:
                print("ERROR! NO PUEDES DIVIDIR ENTRE CERO!\n")
        resultado_division = variable1 / variable2
        print("El resultado de la division es:\n", resultado_division)    
    elif opcion == 5:
        while True:
            try:
                print("Esta seguro que quiere salir del programa?\n")
                opcion = int(input("\n1:Si\n2:No\n"))
                if opcion == 1:
                    print("\nSaliendo del programa...\n")
                    return
                elif opcion == 2:
                    print("\nRegresando al menu...\n")
                    break
                if 1 <= opcion <= 2:
                    break
                print("Debe ingresar 1 o 2 para su desicion\n")
            except ValueError:
                print("Debe ingresar un numero valido\n")
    menu()
menu()
# while True:
#     try:
#         num1 = float(input("ingrese num"))
#         num2 = float(input("ingrese otro num"))
#         if num2 < 0 or num2 > 0:
#             break
#         print("no puedes dividir entre cero")
#     except ZeroDivisionError:
#         print("no puedes dividir entre cero")
# resultado = num1 / num2
# print("resultado", resultado)

    

        
            
        
    


        


    
    



    


            
        

       
    
    
    


    
    
