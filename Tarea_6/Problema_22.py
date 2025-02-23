#22.Simular el lanzamiento de un dado y una moneda.

print("a) Dado")
print("b) Moneda")
opcion = input("Dado o Moneda:")
if opcion == 'a':
    import numpy as np
    cara_dado = int(np.random.uniform(1,7,1))
    print("Cara de dado:",cara_dado)
else:
    import numpy as np
    cara_moneda = int(np.random.uniform(1,3,1))
    if cara_moneda == 1:
        print("Es aguila")
    else:
        print("Es sol")





