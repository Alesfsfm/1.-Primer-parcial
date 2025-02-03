nom = input('ingrese su nombre:\n')

def obtener_altura():
    while True:
        try:
            altura = float(input("Ingrese la altura del triángulo: "))
            if altura > 0:
                return altura
            else:
                print("Error: La altura debe ser mayor a cero. Inténtelo nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

altura = obtener_altura()

def obtener_base():
    while True:
        try:
            Base = float(input("Ingrese la base del triangulo:    "))
            if Base > 0:
                return Base
            else:
                print("Error: La base debe ser mayor a cero")
        except ValueError:
                print("Error: Debe ingresar un numero valido")
        
Base = obtener_base()

area = Base *altura / 2
print("el area del triangulo es:",area )





            

