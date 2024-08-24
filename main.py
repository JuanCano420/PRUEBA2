from flask import Flask, render_template, request, redirect, url_for
from clases.producto import Producto
from clases.categoria import Categoria
from clases.proveedor import Proveedor
from clases.bodega import Bodega

app = Flask(__name__)

# Datos de ejemplo
categorias = [Categoria("Electrónica", "Dispositivos electrónicos y accesorios"),
              Categoria("Ropa", "Prendas de vestir y accesorios")]

productos = [Producto("Laptop", "Laptop de alta gama", 1500, 10, categorias[0]),
             Producto("Camiseta", "Camiseta de algodón", 20, 50, categorias[1])]

proveedores = [Proveedor("TechSupplier", "123 Calle Falsa", "555-1234"),
               Proveedor("ClothesCo", "456 Avenida Real", "555-5678")]

bodegas = [Bodega("Bodega Central", "Zona Industrial", 100),
           Bodega("Bodega Norte", "Zona Norte", 200)]

# Rutas

@app.route('/')
def index():
    return render_template('index.html', productos=productos, categorias=categorias, proveedores=proveedores, bodegas=bodegas)

@app.route('/producto/<nombre>')
def producto(nombre):
    prod = next((p for p in productos if p.nombre == nombre), None)
    return render_template('producto.html', producto=prod)

@app.route('/categoria/<nombre>')
def categoria(nombre):
    cat = next((c for c in categorias if c.nombre == nombre), None)
    return render_template('categoria.html', categoria=cat)

@app.route('/proveedor/<nombre>')
def proveedor(nombre):
    prov = next((p for p in proveedores if p.nombre == nombre), None)
    return render_template('proveedor.html', proveedor=prov)

@app.route('/bodega/<nombre>')
def bodega(nombre):
    bod = next((b for b in bodegas if b.nombre == nombre), None)
    return render_template('bodega.html', bodega=bod)

if __name__ == '__main__':
    app.run(debug=True)
