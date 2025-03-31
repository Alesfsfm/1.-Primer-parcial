import conversor

km = float(input("Ingrese los kilómetros: "))
celsius = float(input("Ingrese la temperatura en Celsius: "))
litros = float(input("Ingrese los litros: "))

print(f"{km} km = {conversor.kilometros_a_millas(km):.2f} millas")
print(f"{celsius}°C = {conversor.celsius_a_fahrenheit(celsius):.2f}°F")
print(f"{litros} L = {conversor.litros_a_galones(litros):.2f} galones")