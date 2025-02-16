# 19. Generar numeros aleatorios con distintas distribuciones
import numpy as np
uniforme = np.random.uniform(1,3,100)
print(uniforme)
normal = np.random.normal(2,3,50)
print(normal)
binomial = np.random.binomial(10,0.1,5)
print(binomial)
