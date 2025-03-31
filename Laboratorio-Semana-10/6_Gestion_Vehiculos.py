class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio
    
    def mostrar_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Precio: ${self.precio}"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, numero_puertas):
        super().__init__(marca, modelo, anio, precio)
        self.numero_puertas = numero_puertas

    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", Puertas: {self.numero_puertas}"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, cilindrada):
        super().__init__(marca, modelo, anio, precio)
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", Cilindrada: {self.cilindrada}cc"

auto = Automovil("Toyota", "Corolla", 2023, 25000, 4)
moto = Motocicleta("Honda", "CBR500R", 2022, 7000, 500)

print(auto.mostrar_informacion())
print(moto.mostrar_informacion())