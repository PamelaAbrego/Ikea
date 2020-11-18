import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="ikea",
    cursorclass=pymysql.cursors.DictCursor,
)


class Registro:
    def __init__(self):
        Username = str(input("Nombre Usuario: "))
        Contrasenna = str(input("Contraseña: "))
        Existe = False
        users = []
        username = []
        try:
            with connection.cursor() as cursor:
                sql = f"select nombreUsuario from ikea.Usuarios;"
                cursor.execute(sql)
                users = cursor.fetchall()
                for user in users:
                    username.append(user["nombreUsuario"])

                Existe = Username in username

                if Existe is True:
                    sql2 = f"select contrasenna from ikea.usuarios where nombreUsuario = '{Username}';"
                    cursor.execute(sql2)
                    resulta = cursor.fetchall()
                    psw2 = resulta[0]
                    password = psw2["contrasenna"]

                    if Contrasenna == password:
                        print("--Ingreso realizado con éxito--")

                    else:
                        print(
                            "El usuario o la contraseña están incorrectas, vuelve a intentarlo"
                        )
                        login()

                else:
                    print(
                        "No se ha encontrado este nombre de usuario, vuelve a intentarlo"
                    )
                    login()

        finally:
            pass
