import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="ikea",
    cursorclass=pymysql.cursors.DictCursor,
)


def getFacturaBD():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = """SELECT facturas.idFacturas, usuarios.idUsuarios, usuarios.nombreUsuario, facturas.tipoDePago, sucursales.idSucursales,
            sucursales.direccion as sucursal, facturas.fecha, facturas.hora, facturas.idCarritos
            FROM ikea.usuarios inner join ikea.facturas on usuarios.idUsuarios = facturas.idUsuarios
            inner join ikea.sucursales on facturas.idSucursales = sucursales.idSucursales"""
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result


def insertFacturasBD(idUsuarios, tipoDePago, idSucursales, fecha, hora, idCarrito):
    try:
        with connection.cursor() as cursor:
            sql = f"""insert into ikea.facturas (idUsuarios, tipoDePago, idSucursales, fecha, hora, idCarritos)
            values ('{idUsuarios}','{tipoDePago}','{idSucursales}','{fecha}','{hora}', '{idCarrito}');"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def searchFacturasById(idFacturas):
    facturas = {}
    try:
        with connection.cursor() as cursor:
            sql = f"select * from ikea.facturas where idFacturas ={idFacturas};"
            cursor.execute(sql)
            facturas = cursor.fetchone()
    finally:
        pass
    return facturas


def updateFacturasBD(
    idUsuarios, tipoDePago, idSucursales, fecha, hora, idCarrito, idFacturas
):
    try:
        with connection.cursor() as cursor:
            sql = f"""UPDATE ikea.facturas SET idUsuarios = '{idUsuarios}',
            tipoDePago = '{tipoDePago}', idSucursales = '{idSucursales}',
            fecha = '{fecha}', hora = '{hora}', idCarritos = '{idCarrito}'
            where idFacturas = '{idFacturas}';"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def deleteFacturasBD(idFacturas):
    try:
        with connection.cursor() as cursor:
            sql = f"delete from ikea.facturas WHERE idFacturas = {idFacturas};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass
