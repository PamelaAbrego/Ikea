import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="ikea",
    cursorclass=pymysql.cursors.DictCursor,
)


def getCategoriaBD():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM ikea.categoriasproductos;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result


def insertCategoriaBD(nombre):
    try:
        with connection.cursor() as cursor:
            sql = f"insert into ikea.categoriasproductos (nombre) values ('{nombre}');"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def searchCategoriaById(idCategoria):
    categoria = {}
    try:
        with connection.cursor() as cursor:
            sql = f"select * from ikea.categoriasproductos where idCategoriasProductos={idCategoria};"
            cursor.execute(sql)
            categoria = cursor.fetchone()
    finally:
        pass
    return categoria


def updateCategoriaBD(nombre, idCategoria):
    try:
        with connection.cursor() as cursor:
            sql = f"UPDATE ikea.categoriasproductos SET nombre = '{nombre}' WHERE idCategoriasProductos = '{idCategoria}';"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def deleteCategoriaBD(idCategoria):
    try:
        with connection.cursor() as cursor:
            sql = f"delete from ikea.categoriasproductos WHERE idCategoriasProductos = {idCategoria};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass
