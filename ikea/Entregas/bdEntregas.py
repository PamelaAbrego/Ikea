import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="ikea",
    cursorclass=pymysql.cursors.DictCursor,
)


def getEntregaBD():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM ikea.entregas;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result


def insertEntregaBD(idFactura, fecha, hora, lugar):
    try:
        with connection.cursor() as cursor:
            sql = f"insert into ikea.entregas (idFacturas, fecha, hora, lugar) values ('{idFactura}','{fecha}','{hora}','{lugar}');"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def searchEntregaById(idEntrega):
    entrega = {}
    try:
        with connection.cursor() as cursor:
            sql = f"select * from ikea.entregas where idEntregas={idEntrega};"
            cursor.execute(sql)
            entrega = cursor.fetchone()
    finally:
        pass
    return entrega


def updateEntregaBD(idFactura, fecha, hora, lugar, idEntrega):
    try:
        with connection.cursor() as cursor:
            sql = f"""UPDATE ikea.entregas SET idFacturas = '{idFactura}', fecha = '{fecha}', hora ='{hora}', lugar = '{lugar}'
            WHERE idEntregas = '{idEntrega}';"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def deleteEntregaBD(idEntrega):
    try:
        with connection.cursor() as cursor:
            sql = f"delete from ikea.entregas WHERE idEntregas = {idEntrega};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass
