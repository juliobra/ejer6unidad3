import json

def cargar_vehiculos(archivo):
    vehiculos = []
    with open(archivo, 'r') as file:
        data = json.load(file)
        for vehiculo_data in data:
            modelo = vehiculo_data["modelo"]
            cantidad_puertas = vehiculo_data["cantidad_puertas"]
            color = vehiculo_data["color"]
            precio_base = vehiculo_data["precio_base"]
            if "version" in vehiculo_data:  # Vehículo nuevo
                version = vehiculo_data["version"]
                vehiculo = VehiculoNuevo(modelo, cantidad_puertas, color, precio_base, version)
            else:  # Vehículo usado
                marca = vehiculo_data["marca"]
                patente = vehiculo_data["patente"]
                año = vehiculo_data["año"]
                kilometraje = vehiculo_data["kilometraje"]
                vehiculo = VehiculoUsado(modelo, cantidad_puertas, color, precio_base, marca, patente, año, kilometraje)
            vehiculos.append(vehiculo)
    return vehiculos

# Cargar los vehículos desde el archivo
vehiculos = cargar_vehiculos("vehiculos.json")

# Menú de opciones
while True:
    print("----- Menú de Opciones -----")
    print("1. Insertar vehículo en la lista en una posición determinada")
    print("2. Agregar un vehículo a la lista")
    print("3. Mostrar tipo de objeto en una posición de la lista")
    print("4. Modificar precio base y mostrar precio de venta de un vehículo usado")
    print("5. Mostrar datos del vehículo más económico")
    print("6. Mostrar datos de todos los vehículos")
    print("0. Salir")

    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        modelo = input("Ingrese el modelo del vehículo: ")
        cantidad_puertas = int(input("Ingrese la cantidad de puertas del vehículo: "))
        color = input("


if __name__=='__main__':
      cargar_vehiculos("vehiculos.jason")
                      









