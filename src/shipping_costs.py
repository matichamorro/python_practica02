
def calculate_costs():
    valid = False
    valid_zones = ["local","regional","nacional"]

    weight = float(input("Ingrese el peso del paquete (kg): "))
    while not valid:
        zone = input("Ingrese la zona de destino (local/regional/nacional): ")
        valid = True if zone in valid_zones else print("Zona no válida. Las zonas disponibles son: local, regional, nacional.")
        
    match weight:
        case x if x <= 1:
            match zone:
                case "local":
                    cost = 500
                case "regional":
                    cost = 1000
                case "nacional":
                    cost = 2000
        case x if 1 < x <= 5:
            match zone:
                case "local":
                    cost = 1000
                case "regional":
                    cost = 2500
                case "nacional":
                    cost = 4500
        case x if x > 5:
            match zone:
                case "local":
                    cost = 2000
                case "regional":
                    cost = 5000
                case "nacional":
                    cost = 8000
    
    print(f"Costo de envío: ${cost}")