#27.Crear un conversor de unidades.
print("a) convertir gramos a kilos")
print("b) convertir metros a kilometros")
opcion = input("que desea convertir")
if opcion == 'a':
    cantidad_masa = float(input("Ingrese la cantidad de gramos"))
    conversion_masa = cantidad_masa/1000
    print(conversion_masa,"kilos")
else:
    cantidad_metros = float(input("Ingrese la cantidad de gramos"))
    conversion_metros = cantidad_metros/1000
    print(conversion_metros,"kilometros")

