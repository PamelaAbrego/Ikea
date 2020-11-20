import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="ikea",
    cursorclass=pymysql.cursors.DictCursor,
)


class RegistroNuevaCuenta:
    def __init__(self):
        self.registroNuevaCuenta()

    def registroNuevaCuenta(self):
        print("Crearás un nuevo Usuario:")
        name = input("Nombre: ")
        apellido = input("Apellido: ")
        segundoApellido = input("Segundo apellido: ")
        username = input("Usuario: ")
        telefono = input("Número de teléfono: ")
        idioma = input("Idioma: ")
        correoElectronico = input("Correo electrónico: ")
        contrasenna = input("Contraseña: ")
        contrasenna2 = input("Confirma tu contraseña: ")
        direccion = input("Dirección: ")
        Existe = False
        users = []
        usuarios = []

        if contrasenna == contrasenna2:
            try:
                with connection.cursor() as cursor:
                    sql = f"select nombreUsuario from ikea.Usuarios;"
                    cursor.execute(sql)
                    users = cursor.fetchall()
                    for user in users:
                        usuarios.append(user["nombreUsuario"])
                    Existe = username in usuarios

                    if Existe is True:
                        print("---------------------------------------------------")
                        print(
                            "Este nombre de usuario ya está registrado. Vuelve a intentarlo"
                        )
                        print("---------------------------------------------------")
                        self.registroNuevaCuenta()

                    else:
                        sql = f"""insert into ikea.usuarios (nombreUsuario, nombre, apellido, segundoApellido, telefono,
                            idioma, correoElectronico, contrasenna, direccion) values ('{username}','{name}','{apellido}',
                            '{segundoApellido}','{telefono}','{idioma}','{correoElectronico}','{contrasenna}', '{direccion}');"""
                        cursor.execute(sql)
                        connection.commit()
                        print("-----------Se agregó correctamente el usuario----------")
            finally:
                pass
        else:
            print("---------------------------------------------------")
            print("Las contraseñas ingresadas no corresponden. Vuelve a intentarlo")
            print("---------------------------------------------------")
            self.registroNuevaCuenta()
