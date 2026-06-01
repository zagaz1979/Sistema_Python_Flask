from models.producto_model import (
    obtener_todos_los_productos,
    insertar_producto,
    eliminar_producto,
)


def listar_productos():
    return obtener_todos_los_productos()


def crear_producto(nombre, precio, stock):
    insertar_producto(nombre, precio, stock)


def borrar_producto(product_id):
    eliminar_producto(product_id)
