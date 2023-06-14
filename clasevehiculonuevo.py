class VehiculoNuevo(Vehiculo):
    def __init__(self, modelo, cantidad_puertas, color, precio_base, version):
        super().__init__(modelo, cantidad_puertas, color, precio_base)
        self.version = version

    def calcular_importe_venta(self):
        importe_venta = self.precio_base + (self.precio_base * 0.1)  # Agregar 10% por gastos de patentamiento
        if self.version == "full":
            importe_venta += self.precio_base * 0.02  # Agregar 2% si es versión full
        return importe_venta