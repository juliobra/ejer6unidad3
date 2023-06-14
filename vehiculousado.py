class VehiculoUsado(Vehiculo):
    def __init__(self, modelo, cantidad_puertas, color, precio_base, marca, patente, año, kilometraje):
        super().__init__(modelo, cantidad_puertas, color, precio_base)
        self.marca = marca
        self.patente = patente
        self.año = año
        self.kilometraje = kilometraje

    def calcular_importe_venta(self):
        importe_venta = self.precio_base - (self.precio_base * 0.01 * (2023 - self.año))  # Restar 1% por cada año de antigüedad
        if self.kilometraje > 100000:
            importe_venta -= self.precio_base * 0.02  # Restar 2% si el kilometraje supera los 100.000
        return importe_venta