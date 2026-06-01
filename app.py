from flask import Flask, render_template, request, redirect
from controllers.producto_controller import (
    listar_productos,
    crear_producto,
    borrar_producto,
)

app = Flask(__name__)


# HOME
@app.route("/")
def home():
    return redirect("/productos")


# LISTAR PRODUCTOS
@app.route("/productos")
def productos():
    data = listar_productos()
    return render_template("productos.html", productos=data)


# CREAR PRODUCTO
@app.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = request.form["precio"]
        stock = request.form["stock"]

        crear_producto(nombre, precio, stock)
        return redirect("/productos")

    return render_template("crear_producto.html")


# ELIMINAR PRODUCTO
@app.route("/eliminar/<int:id>")
def eliminar(id):
    borrar_producto(id)
    return redirect("/productos")


if __name__ == "__main__":
    app.run(debug=True)
