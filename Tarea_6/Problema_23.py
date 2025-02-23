#23.Implementar y operar con matrices.
import numpy as np
M1 = np.array([[1,3] , [5,7]])
M2 = np.array([[6,5] , [7,8]])
Suma = np.add(M1, M2)
Multiplicacion = np.dot(M1,M2)
Resta = np.subtract(M1,M2)
InversaM1 = np.linalg.inv(M1)
InversaM2 = np.linalg.inv(M2)
TranspuestaM1 = np.transpose(M1)
TranspuestaM2 = np.transpose(M2)
DeterminanteM1 = np.linalg.det(M1)
DeterminanteM2 = np.linalg.det(M2)
print("Suma\n", Suma)
print("Multiplicacion\n", Multiplicacion)
print("Resta\n", Resta)
print("InversaM1\n", InversaM1)
print("InversaM2\n",InversaM2)
print("TranspuestaM1\n", TranspuestaM1)
print("TranspuestaM2\n", TranspuestaM2)
print("DeterminanteM1\n", round(DeterminanteM1))
print("DeterminanteM2\n", round(DeterminanteM2))



