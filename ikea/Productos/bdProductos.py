import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="ikea",
    cursorclass=pymysql.cursors.DictCursor,
)


def getProductoBD():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = """SELECT productos.idProductos, productos.nombre, productos.precio, productos.dimensiones,
            productos.materiales, productos.coloresDisponibles, productos.descripcion, productos.garantia,
            claseproductos.idClaseProductos ,claseproductos.nombre as nombreClaseProductos
            FROM ikea.productos inner join ikea.claseproductos on
            productos.idClaseProductos = claseproductos.idClaseProductos;"""
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result


def insertProductoBD(
    nombre,
    precio,
    dimensiones,
    materiales,
    coloresDisponibles,
    descripcion,
    garantia,
    idClaseProducto,
):
    try:
        with connection.cursor() as cursor:
            sql = f"""insert into ikea.productos (nombre, precio, dimensiones, materiales, coloresDisponibles, descripcion, garantia, idClaseProductos)
            values ('{nombre}','{precio}','{dimensiones}','{materiales}','{coloresDisponibles}','{descripcion}','{garantia}','{idClaseProducto}');"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def searchProductoById(idProducto):
    producto = {}
    try:
        with connection.cursor() as cursor:
            sql = f"select * from ikea.productos where idProductos={idProducto};"
            cursor.execute(sql)
            producto = cursor.fetchone()
    finally:
        pass
    return producto


def updateProductoBD(
    nombre,
    precio,
    dimensiones,
    materiales,
    coloresDisponibles,
    descripcion,
    garantia,
    idClaseProducto,
    idProducto,
):
    try:
        with connection.cursor() as cursor:
            sql = f"""UPDATE ikea.productos SET nombre = '{nombre}', precio = '{precio}',
            dimensiones = '{dimensiones}', materiales = '{materiales}', coloresDisponibles = '{coloresDisponibles}',
            descripcion = '{descripcion}', garantia = '{garantia}', idClaseProductos = '{idClaseProducto}'
            where idProductos = '{idProducto}';"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def deleteProductoBD(idProducto):
    try:
        with connection.cursor() as cursor:
            sql = f"delete from ikea.productos WHERE idProductos = {idProducto};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass
