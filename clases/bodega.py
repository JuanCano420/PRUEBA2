class Bodega:
    def __init__(self, nombre, ubicacion, capacidad_maxima):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima
        self.productos_almacenados = {}

    def agregar_producto(self, producto, cantidad):
        if self.capacidad_disponible() >= cantidad:
            if producto in self.productos_almacenados:
                self.productos_almacenados[producto] += cantidad
            else:
                self.productos_almacenados[producto] = cantidad
            return True
        else:
            return False

    def retirar_producto(self, producto, cantidad):
        if producto in self.productos_almacenados and self.productos_almacenados[producto] >= cantidad:
            self.productos_almacenados[producto] -= cantidad
            if self.productos_almacenados[producto] == 0:
                del self.productos_almacenados[producto]
            return True
        else:
            return False

    def capacidad_disponible(self):
        return self.capacidad_maxima - sum(self.productos_almacenados.values())

    def consultar_disponibilidad(self, producto):
        return self.productos_almacenados.get(producto, 0)

    def __str__(self):
        return f"Bodega(nombre={self.nombre}, capacidad_disponible={self.capacidad_disponible()})"
