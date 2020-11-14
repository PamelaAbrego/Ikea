import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="ikea",
    cursorclass=pymysql.cursors.DictCursor,
)


def getClaseBD():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = """SELECT claseproductos.idClaseProductos, claseproductos.nombre,
            categoriasproductos.idCategoriasProductos, categoriasproductos.nombre as nombreCategoriaProducto
            FROM ikea.claseproductos inner join ikea.categoriasproductos on
            claseproductos.idCategoriasProductos= categoriasproductos.idCategoriasProductos;"""
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result


def insertClaseBD(nombre, idCategoria):
    try:
        with connection.cursor() as cursor:
            sql = f"insert into ikea.claseproductos (nombre, idCategoriasProductos) values ('{nombre}', '{idCategoria}');"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def searchClaseById(idClase):
    clase = {}
    try:
        with connection.cursor() as cursor:
            sql = (
                f"SELECT * FROM ikea.claseproductos where idClaseProductos ='{idClase}'"
            )
            cursor.execute(sql)
            clase = cursor.fetchone()
    finally:
        pass
    return clase


def updateClaseBD(nombre, idCategoria, idClase):
    try:
        with connection.cursor() as cursor:
            sql = f"UPDATE ikea.claseproductos SET nombre = '{nombre}', idCategoriasProductos = '{idCategoria}' where idClaseProductos = '{idClase}';"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def deleteClaseBD(idClase):
    try:
        with connection.cursor() as cursor:
            sql = f"delete from ikea.claseproductos WHERE idClaseProductos = {idClase};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass
