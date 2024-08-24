class Proveedor:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos_suministrados = []

    def agregar_producto(self, producto):
        if producto not in self.productos_suministrados:
            self.productos_suministrados.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.productos_suministrados:
            self.productos_suministrados.remove(producto)

    def __str__(self):
        return f"Proveedor(nombre={self.nombre}, productos_suministrados={len(self.productos_suministrados)})"
