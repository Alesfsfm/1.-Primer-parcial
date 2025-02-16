kuger_papa = 0
kuger_arroz = 0
papa = str
arroz = str
Si = str
No = str
opcion = str
def menu():
    global kuger_papa, kuger_arroz
    while True:
        try:
            print("Hay clientes a registrar?\n")
            opcion = str(input("Si / No\n"))
            if opcion == "Si":
                input("Ingrese el tipo de kuger que el cliente ha elegido:\n")
                print("Kuger de arroz: 'arroz'\n")
                print("Kuger de papa: 'papa'\n")
                kuger = str(input("Ingrese la palabra papa o arroz para registrar el tipo de kuger:\n"))
                while True:
                        kuger = input("Ingrese 'papa' o 'arroz' para registrar el tipo de kuger:\n").strip()
                        if kuger == "papa":
                            kuger_papa += 1
                            break
                        elif kuger == "arroz":
                            kuger_arroz += 1
                            break
                        else:
                            print("Debe ingresar 'papa' o 'arroz':\n")
                print("cantidad total vendidas kuger de papa:", kuger_papa)
                print("cantidad total vendidas kuger de arroz:", kuger_arroz)
            elif opcion == "No":
                salir = str(input("Desea salir del programa? Si/No\n"))
                while True:
                    try:
                        if salir == "Si":
                            print("Saliendo de la base de datos...\n")
                            return
                        elif salir == "No":
                            print("Volviendo a la base de datos...\n")
                            break
                        if salir == "Si" or salir == "No":
                            break
                        print("Debe ingresar 'Si' o 'Si' para su respuesta:\n")
                    except IndexError:
                        print("Debe ingresar 'No' o 'No' para su respuesta:\n")
            if opcion == "Si" or opcion == "No":
                break
            print("Debe ingresar 'Si' o 'No' para su respuesta:\n")
        except IndexError:
            print("Debe ingresar 'Si' o 'No' para su respuesta:\n")
    menu()
menu()

            
