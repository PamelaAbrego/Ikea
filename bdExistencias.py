import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="ikea",
    cursorclass=pymysql.cursors.DictCursor,
)


def getExistenciaBD():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = """SELECT existencias.idExistencias, productos.idProductos, productos.nombre as producto, sucursales.idSucursales, sucursales.direccion as sucursal, cantidad
            FROM ikea.productos inner join ikea.existencias on productos.idProductos = existencias.idProductos
            inner join ikea.sucursales on existencias.idSucursales = sucursales.idSucursales;"""
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result


def insertExistenciaBD(idProducto, idSucursal, cantidad):
    try:
        with connection.cursor() as cursor:
            sql = f"insert into ikea.existencias (idProductos, idSucursales, cantidad) values ('{idProducto}', '{idSucursal}','{cantidad}');"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def searchExistenciaById(idExistencia):
    existencia = {}
    try:
        with connection.cursor() as cursor:
            sql = (
                f"SELECT * FROM ikea.existencias where idExistencias ='{idExistencia}'"
            )
            cursor.execute(sql)
            existencia = cursor.fetchone()
    finally:
        pass
    return existencia


def updateExistenciaBD(idProducto, idSucursal, cantidad, idExistencia):
    try:
        with connection.cursor() as cursor:
            sql = f"UPDATE ikea.existencias SET idProductos = '{idProducto}', idSucursales= '{idSucursal}', cantidad='{cantidad}' where idExistencias= '{idExistencia}';"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def deleteExistenciaBD(idExistencia):
    try:
        with connection.cursor() as cursor:
            sql = f"delete from ikea.existencias WHERE idExistencias = {idExistencia};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass
