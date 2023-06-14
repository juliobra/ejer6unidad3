class ListaVehiculos:
    def __init__(self):
        self.vehiculos = []

    def insertar_vehiculo(self, vehiculo, posicion):
        self.vehiculos.insert(posicion, vehiculo)

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrar_tipo_vehiculo(self, posicion):
        vehiculo = self.vehiculos[posicion]
        if isinstance(vehiculo, VehiculoNuevo):
            print("El vehículo en la posición", posicion, "es un Vehículo Nuevo")
        elif isinstance(vehiculo, VehiculoUsado):
            print("El vehículo en la posición", posicion, "es un Vehículo Usado")

    def modificar_precio_venta(self, patente, nuevo_precio_base):
        for vehiculo in self.vehiculos:
            if isinstance(vehiculo, VehiculoUsado) and vehiculo.patente == patente:
                vehiculo.precio_base = nuevo_precio_base
                print("El nuevo precio de venta del vehículo usado con patente", patente, "es:", vehiculo.calcular_importe_venta())
                break

    def vehiculo_mas_economico(self):
        vehiculo_mas_economico = None
        for vehiculo in self.vehiculos:
            if not vehiculo_mas_economico or vehiculo.calcular_importe_venta() < vehiculo_mas_economico.calcular_importe_venta():
                vehiculo_mas_economico = vehiculo
        if vehiculo_mas_economico:
            print("Datos del vehículo más económico:")
            print("Modelo:", vehiculo_mas_economico.modelo)
            print("Cantidad de puertas:", vehiculo_mas_economico.cantidad_puertas)
            print("Precio de venta:", vehiculo_mas_economico.calcular_importe_venta())
        else:
            print("No hay vehículos en la lista")

    def mostrar_vehiculos(self):
        for vehiculo in self.vehiculos:
            print("Modelo:", vehiculo.modelo)
            print("Cantidad de puertas:", vehiculo.cantidad_puertas)
            print("Precio de venta:", vehiculo.calcular_importe_venta())
            print()

# Crear la lista de vehículos
lista_vehiculos = ListaVehiculos()

# Agregar los vehículos a la lista
for vehiculo in vehiculos:
    lista_vehiculos.agregar_vehiculo(vehiculo)
