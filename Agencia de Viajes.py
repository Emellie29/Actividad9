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
                print("☺☺☺Destinos turísticos☺☺☺")
                clientes[codigo] = {
                    "nombre": nombre,
                    "destinos": [],
                    "codigo": codigo
                }
                destinoT= int(input("Ingrese la cantidad de Destinos: "))
                for _ in range(destinoT):
                    lugar= input("Nombre del destino: ")
                    clientes[codigo]["destinos"].append(lugar)
                    print(f"Destino {lugar} guardado con éxito")
        case "2":
            print("Listado de Clientes con sus Destinos")
            for codigo, datos in clientes.items():
                print(f"\nCódigo: {codigo}")
                print(f"Nombre: {datos["nombre"]}")
                print(f"Destino: ")
                for destinos in datos['destinos']:
                    print(f" ► {destinos}")
        case "3":
            def contar_destinos(lista, indice=0):
                if indice == len(lista):
                    return 0
                d_actual = len(lista[indice]["destinos"])
                return d_actual + contar_destinos(lista, indice + 1)
            total = contar_destinos(list(clientes.values()))
            print(f"Total de destinos: {total}")
        case "4":
            def cliente_viajero(clientes):
                max_destinos=-1
                cliente_top= ""
                for datos in clientes.values():
                    cantidad = len(datos["destinos"])
                    if cantidad > max_destinos:
                        max_destinos = cantidad
                        cliente_top = datos["nombre"]
                return cliente_top, max_destinos
            nombre, cantidad = cliente_viajero(clientes)
            print(f"Cliente con más destinos: {nombre} con {cantidad} destinos")
        case "5":
            print("Salir")
            break
        case _:
            print("Opcion no valida. Intente de nuevo.")