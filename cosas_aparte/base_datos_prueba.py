kuger_papa = 0
kuger_arroz = 0

def menu():
    global kuger_papa, kuger_arroz  # Declaramos globales para modificar su valor dentro de la función
    
    while True:
        try:
            print("Hay clientes a registrar?\n")
            opcion = input("Si / No\n").strip()

            if opcion == "Si":
                print("Ingrese el tipo de kuger que el cliente ha elegido:")
                print("Kuger de arroz: 'arroz'\nKuger de papa: 'papa'\n")

                while True:
                    kuger = input("Ingrese 'papa' o 'arroz' para registrar el tipo de kuger:\n").strip()
                    
                    if kuger == "papa":
                        kuger_papa += 1
                        break
                    elif kuger == "arroz":
                        kuger_arroz += 1
                        break
                    else:
                        print("Debe ingresar 'papa' o 'arroz'. Inténtelo nuevamente.\n")

                print("Cantidad total de kuger de papa vendidas:", kuger_papa)
                print("Cantidad total de kuger de arroz vendidas:", kuger_arroz)

            elif opcion == "No":
                while True:
                    salir = input("Desea salir del programa? Si/No\n").strip()
                    
                    if salir == "Si":
                        print("Saliendo de la base de datos...\n")
                        return
                    elif salir == "No":
                        print("Volviendo al menú...\n")
                        break
                    else:
                        print("Debe ingresar 'Si' o 'No' para su respuesta.\n")

            else:
                print("Debe ingresar 'Si' o 'No' para su respuesta.\n")

        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

# Ejecutar el menú
menu()
