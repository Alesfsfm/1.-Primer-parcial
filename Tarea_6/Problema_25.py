#25.Generar y analizar histogramas de datos.
import numpy as np
import matplotlib.pyplot as plt

def km_gas():
    km = np.arange(1, 21)  
    gas = km * 5           
    return km, gas

km, gas = km_gas()

plt.bar(km, gas, color='skyblue', edgecolor='black')
plt.xlabel('Kilómetros')
plt.ylabel('Litros de gasolina')
plt.title('Consumo de gasolina por kilómetros')
plt.ylim(0, 100)  

plt.show()
