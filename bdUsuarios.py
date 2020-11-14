import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="ikea",
    cursorclass=pymysql.cursors.DictCursor,
)


def getUsuarioBD():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM ikea.usuarios;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result


def insertUsuarioBD(
    nombreUsuario,
    nombre,
    apellido,
    segundoApellido,
    telefono,
    idioma,
    correoElectronico,
    contrasenna,
    direccion,
):
    try:
        with connection.cursor() as cursor:
            sql = f"""insert into ikea.usuarios (nombreUsuario, nombre, apellido, segundoApellido, telefono, idioma, correoElectronico, contrasenna, direccion)
            values ('{nombreUsuario}','{nombre}','{apellido}', '{segundoApellido}', '{telefono}', '{idioma}', '{correoElectronico}', '{contrasenna}', '{direccion}');"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def searchUsuarioById(idUsuario):
    usuario = {}
    try:
        with connection.cursor() as cursor:
            sql = f"select * from ikea.usuarios where idUsuarios={idUsuario};"
            cursor.execute(sql)
            usuario = cursor.fetchone()
    finally:
        pass
    return usuario


def updateUsuarioBD(
    nombreUsuario,
    nombre,
    apellido,
    segundoApellido,
    telefono,
    idioma,
    correoElectronico,
    contrasenna,
    direccion,
    idUsuario,
):
    try:
        with connection.cursor() as cursor:
            sql = f"""UPDATE ikea.usuarios SET nombreUsuario = '{nombreUsuario}',nombre = '{nombre}',apellido = '{apellido}', segundoApellido ='{segundoApellido}',
            telefono = '{telefono}', idioma='{idioma}', correoElectronico = '{correoElectronico}', contrasenna = '{contrasenna}', direccion = '{direccion}'
            WHERE idUsuarios = '{idUsuario}';"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def deleteUsuarioBD(idUsuario):
    try:
        with connection.cursor() as cursor:
            sql = f"delete from ikea.usuarios WHERE idUsuarios = {idUsuario};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass
