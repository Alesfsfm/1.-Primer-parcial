#13. Convertir una temperatura a distintas escalas.
Temperatura_Inicial = float
Temperatura_Conversion = float
Celsius= float
Fahrenheit = float
Kelvin=float

def menu():
    print("ELIJA EL TIPO DE ESCALA A INGRESAR:\n")
    print("Celcius: 'C'")
    print("Fahrenheit: 'F'")
    print("Kelvin: 'K'")
    while True:
        Eleccion = input("Ingrese el tipo de escala de temperatura que quiera convertir, C: Celcius, F:Fahrenheit, K:Kelvin:\n") 
        if Eleccion == 'C':
            while True:
                try:
                    Celsius = float(input("Ingrese los grados de temperatura:"))
                    print("Conversion Celsius a Kelvin:", Celsius + 273.15)
                    print("Conversion Celsius a Fahrenheit:", (Celsius*(9/5))+32)
                    break
                except ValueError:
                    print("Debe ingresar un numero valido:")
            break
        elif Eleccion == 'F':
            while True:
                try:
                    Fahrenheit = float(input("Ingrese los grados de temperatura:"))
                    print("Conversion Fahrenheit a Celsius:", (Fahrenheit-32)*(5/9))
                    print("Conversion Fahrenheit a Kelvin:",[(5/9)*(Fahrenheit-32)+32])
                    break
                except ValueError:
                    print("Debe ingresar un numero valido:")
            break
        elif Eleccion == 'K':
            while True:
                try:
                    Kelvin = float(input("Ingrese los grados de temperatura:"))
                    print("Conversion Kelvin a Fahrenheit:", [(9/5)*(Kelvin-273)+32])
                    print("Conversion Kelvin a Celsius:", Kelvin - 273.15)
                    break
                except ValueError:
                    print("Debe ingresar un numero valido:")
            break
        else:
                print("Ingrese; C: Celcius, F:Fahrenheit, K:Kelvin")
    
    
    

                  
menu()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def menu():
    #     while True:
    #         try:
    #             print("ELIJA EL TIPO DE ESCALA A CONVERTIR:\n")
    #             print("Celcius: 'C'")
    #             print("Fahrenheit: 'F'")
    #             print("Kelvin: 'K'")
    #             Eleccion2 = input("Ingrese el tipo de escala de temperatura que quiera convertir, C: Celcius, F:Fahrenheit, K:Kelvin:\n")
    #             if Eleccion2 == 'C':
    #                 Temperatura_Inicial == C
    #             elif Eleccion2 == 'F':
    #                 Temperatura_Inicial == F
    #             elif Eleccion2 == 'K':
    #                 Temperatura_Inicial == K
    #             break
    #         except IndexError:
    #             print("C: Celcius, F:Fahrenheit, K:Kelvin")
             
    
    




            