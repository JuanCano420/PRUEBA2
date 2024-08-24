class Producto:
    def __init__(self, nombre, descripcion, precio, stock, categoria=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def agregar_stock(self, cantidad):
        self.stock += cantidad

    def retirar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            return False

    def valor_total(self):
        return self.precio * self.stock

    def __str__(self):
        return f"Producto(nombre={self.nombre}, stock={self.stock}, precio={self.precio})"
