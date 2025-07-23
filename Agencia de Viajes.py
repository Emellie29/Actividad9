clientes={}
while True:
    print("♦♦♦♦♦♦Agencia de Viajes♦♦♦♦♦♦")
    print("1. Registrar Clientes")
    print("2. Listado de Clientes con su destino")
    print("3. Total de destinos")
    print("4. Clientes con más destinos")
    print("5. Salir")
    opcion=input("Selecciona una opción: ")
    match opcion:
        case "1":
            print("Registrar Clientes")
            cantidad = int(input("Ingrese la cantidad de Clientes: "))
            for i in range(cantidad):
                print(f"\nCliente No.{i + 1}")
                codigo = int(input("Codigo de cliente: "))
                nombre = input("Nombre del cliente: ")
                print("Lista de destinos turísticos visitados")
                destinos={}
                destinoT= int(input("Ingrese la cantidad de destinos: "))
                for _ in range(destinoT):
                    lugares= input("Nombre del destino: ")
                    print(f"Destino {lugares} guardado con éxito")
                clientes[codigo] = {
                    "nombre": nombre,
                    "destinos": destinos,
                    "codigo": codigo
                }
        case "2":
            print("Listado de Clientes con su destino")
        case "3":
            print("Total de destinos")
        case "4":
            print("Clientes con más destinos")
        case "5":
            print("Salir")
            break
        case _:
            print("Opcion no valida. Intente de nuevo.")