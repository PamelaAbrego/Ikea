import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="ikea",
    cursorclass=pymysql.cursors.DictCursor,
)


def getPaisBD():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM ikea.paises;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result


def insertPaisBD(nombre):
    try:
        with connection.cursor() as cursor:
            sql = f"insert into ikea.paises (nombre) values ('{nombre}');"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def searchPaisById(idPais):
    pais = {}
    try:
        with connection.cursor() as cursor:
            sql = f"select * from ikea.paises where idPaises={idPais};"
            cursor.execute(sql)
            pais = cursor.fetchone()
    finally:
        pass
    return pais


def updatePaisBD(nombre, idPais):
    try:
        with connection.cursor() as cursor:
            sql = f"UPDATE ikea.paises SET nombre = '{nombre}' WHERE idPaises = '{idPais}';"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def deletePaisBD(idPais):
    try:
        with connection.cursor() as cursor:
            sql = f"delete from ikea.paises WHERE idPaises = {idPais};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass
