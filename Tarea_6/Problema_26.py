#26.Implementar una agenda de contactos.
i = 1
Directorio = list()

while True:    
    Opcion = input(f"Cantidad de contactos: {i-1} \n Desea agregar un contacto?(S/N): ")
    if Opcion== 's':
        contacto = dict()
        contacto["Nombre"] = input(f"Ingrese el nombre de contacto {i}: ")
        contacto["numero"] = input(f"Ingrese el numero de contacto {i}: ")
        i += 1
        Directorio.append(contacto)
    else:
        break
print(Directorio)