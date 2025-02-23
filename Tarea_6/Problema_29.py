#29.Generar y analizar datos estadısticos.
import numpy as np
import pandas as pd

n = 1000  
media = 50  
desviacion_estandar = 15  

datos = np.random.normal(media, desviacion_estandar, n)

df = pd.DataFrame(datos, columns=["Datos"])

media = df["Datos"].mean()
mediana = df["Datos"].median()
desviacion_estandar = df["Datos"].std()
varianza = df["Datos"].var()
minimo = df["Datos"].min()
maximo = df["Datos"].max()

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Desviación Estándar: {desviacion_estandar}")
print(f"Varianza: {varianza}")
print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}")

import matplotlib.pyplot as plt

plt.hist(df["Datos"], bins=30, edgecolor="black")
plt.title("Histograma de Datos Generados")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()
