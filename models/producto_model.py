from config import conexion


# LISTAR PRODUCTOS
def obtener_todos_los_productos():
    db = conexion()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos")
    return cursor.fetchall()


# CREAR PRODUCTO
def insertar_producto(nombre, precio, stock):
    db = conexion()
    cursor = db.cursor()
    sql = (
        "INSERT INTO productos (nombre, precio, stock, estado) VALUES (%s, %s, %s, %s)"
    )
    cursor.execute(sql, (nombre, precio, stock, True))
    db.commit()


# ELIMINAR PRODUCTO
def eliminar_producto(product_id):
    db = conexion()
    cursor = db.cursor()
    cursor.execute("DELETE FROM productos WHERE id=%s", (product_id,))
    db.commit()
