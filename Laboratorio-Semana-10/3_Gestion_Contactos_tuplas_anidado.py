def menu():
    agenda = []

    while True:
        print("1. Agregar contacto")
        print("2. Buscar contacto por nombre")
        print("3. Listar contactos en orden alfabético")
        print("4. Salir")

        opcion = input()

        if opcion == '1':
            nombre = input("Ingrese el nombre: ")
            numero = input("Ingrese el número: ")
            correo = input("Ingrese el correo: ")
            contacto = (nombre, numero, correo)
            agenda.append(contacto)
            print("Contacto agregado correctamente. \n ", agenda)

        elif opcion == '2': 
            nombre_buscar = input("Ingrese el nombre a buscar: ")
            encontrados = [i for i in agenda if i[0].lower() == nombre_buscar.lower()]
            
            if encontrados:
                for i in encontrados:
                    print(f"Nombre: {i[0]}, Número: {i[1]}, Correo: {i[2]}")
            else:
                print("Contacto no encontrado.")

        elif opcion == '3':
            for i in sorted(agenda, key=lambda x: x[0].lower()):
                print(f"Nombre: {i[0]}, Número: {i[1]}, Correo: {i[2]}")

        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()