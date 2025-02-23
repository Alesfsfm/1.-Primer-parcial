#21.Calcular el area y volumen de distintas figuras geometricas.
print("a) Area Triangulo.")
print("b) Area Cuadrado.")
print("c) Volumen Cubo.")
print("d) Volumen Cilindro.")
opcion = input("\nIngrese la figura o prisma dado que desee:\n")
while True:
    try:
        if opcion == 'a':
            Base = float(input("Ingrese la base del triangulo:\n"))
            Altura = float(input("Ingrese la altura del triangulo:\n"))
            Area_Triangulo = (Base*Altura)/2
            print("El area del triangulo fue:", Area_Triangulo)
        elif opcion== 'b':
            Lado = float(input("Ingrese un lado del cuadrado:\n"))
            Area_Cuadrado = Lado**2
            print("El area del cuadrado fue:", Area_Cuadrado)
        elif opcion == 'c':
            Lado_Cubo = float(input("Ingrese un lado del cubo\n"))
            Volumen_Cubo = Lado_Cubo**3
            print("El volumen del cubo fue:", Volumen_Cubo)
        else:
            from math import pi
            radio = float(input("Ingrese el radio:\n"))
            Altura_Cilindro = float(input("ingrese la altura del cilindro:\n"))
            Volumen_Cilindro = pi*(radio**2)*Altura_Cilindro
            print("El volumen del cilindro fue:", Volumen_Cilindro)
    except IndexError:
        print("Debe elegir entre, a), b), c) y d) como sus opciones:\n")


            
