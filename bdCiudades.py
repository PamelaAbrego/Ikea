import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="ikea",
    cursorclass=pymysql.cursors.DictCursor,
)


def getCiudadBD():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = """SELECT ciudades.idCiudades, ciudades.nombre, ciudades.idPaises, paises.nombre as nombrePais
                    FROM ikea.ciudades inner join ikea.paises on
                    ciudades.idPaises= paises.idPaises;"""
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result


def insertCiudadBD(nombre, idPais):
    try:
        with connection.cursor() as cursor:
            sql = f"insert into ikea.ciudades (nombre, idPaises) values ('{nombre}', '{idPais}');"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def searchCiudadById(idCiudad):
    ciudad = {}
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM ikea.ciudades where idCiudades ='{idCiudad}'"
            cursor.execute(sql)
            ciudad = cursor.fetchone()
    finally:
        pass
    return ciudad


def updateCiudadBD(nombre, idPais, idCiudad):
    try:
        with connection.cursor() as cursor:
            sql = f"UPDATE ikea.ciudades SET nombre = '{nombre}', idPaises = '{idPais}' where idCiudades= '{idCiudad}';"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def deleteCiudadBD(idCiudad):
    try:
        with connection.cursor() as cursor:
            sql = f"delete from ikea.ciudades WHERE idCiudades = {idCiudad};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass
