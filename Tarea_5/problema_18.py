# 18. Resolver ecuaciones cuadraticas
a = float(input("ingrese el coeficiente de a:\n"))
b = float(input("ingrese el coeficiente de b:\n"))
c = float(input("ingrese la constante c:\n"))

Resultado_x1 = ((-b+(b**2-4*a*c)**0.5)/(2*a))
print(Resultado_x1)
Resultado_x2 = ((-b-(b**2-4*a*c)**0.5)/(2*a))
print(Resultado_x2)
