def menu():
    ListaProductos = []

    while True:
        print("\n1- Registrar productos")
        print("2- Eliminar productos")
        print("3- Buscar productos")
        print("4- Mostrar precios")
        print("5- Salir")

        Eleccion = input("Seleccione una opción: ")

        if Eleccion == '1':
            producto = {
                "Nombre": input("Ingrese el nombre del producto: "),
                "Categoria": input("Ingrese la categoría del producto: "),
                "Precio": float(input("Ingrese el precio del producto: ")),
                "Cantidad": int(input("Ingrese la cantidad del producto: "))
            }
            ListaProductos.append(producto)
            print("Producto registrado.")

        elif Eleccion == '2':
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            ListaProductos = [i for i in ListaProductos if i['Nombre'].lower() != nombre.lower()]
            print("Producto eliminado.")

        elif Eleccion == '3':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            for i in ListaProductos:
                if i['Nombre'].lower() == nombre.lower():
                    print(i)
                    break
            else:
                print("Producto no encontrado.")

        elif Eleccion == '4':
            for i in sorted(ListaProductos, key=lambda x: x['Precio']):
                print(f"Nombre: {i['Nombre']}, Precio: {i['Precio']}, Cantidad: {i['Cantidad']}")

        elif Eleccion == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")
menu()
