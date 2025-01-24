
def menu(): 
    while True:
        print("1. cubo\n")
        print("2. triangulo\n")
        print("3. cuadrado\n")
        print("4. rectangulo\n")
        print("5. salir\n")
        def confirmacion():
            while True:
                try:
                    opcion = input("elija un numero entre 1 y 5 \n")
                    if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:
                    return opcion
                  else:
                print("elija un numero entre 1 y 5\n")
                except ValueError:
        print("debe elejir un nuemro entre 1 y 5\n")
        opcion = confirmacion():

    
        
        
        if opcion == "1":
            def submenu():
                while True:
                    print("1. Calcular volumen\n")
                    print("2. salir\n")
                    opcion_submenu_1 = input("elija entre el 1 y el 2")
                    if opcion_submenu_1 == "1":
                        def longitud_cubo():
                            while True:
                                try:
                                    lado_cubo = float(input("ingrese la longitud de un lado cualesquiera del cubo\n"))
                                    if lado_cubo > 0:
                                        return lado_cubo
                                    else:
                                        print("elija una medida mayor a cero\n")
                                except ValueError:
                                    print("debe de elejir un numero mayor a cero\n")
                        lado_cubo = longitud_cubo()
                        volumen = lado_cubo^3
                        print("el volumen del cubo es:",volumen)
                    if opcion_submenu_1 == "2":
                        exit()     
menu()




                        
