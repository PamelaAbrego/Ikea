from registro import Registro
from usuarios_view import tablaUsuarios
from menuClientes import MenuClientes


class MenuRegistro:
    def __init__(self):
        while True:
            print("Bienvenido a la tienda IKEA")
            print("Registro:")
            print("0 - Regresar.")
            print("1 - Ingresar con una cuenta existente.")
            print("2 - Crear nueva cuenta.")

            option = int(input("Opción: "))

            if option == 0:
                print("------------------------------------------")
                print("Saliendo de modo Cliente.")
                print("------------------------------------------")
                break
            if option == 1:
                print("------------------------------------------")
                print("--Ingreso con cuenta existente--")
                Registro()
                MenuClientes()
                print("------------------------------------------")
            if option == 2:
                usuarios = tablaUsuarios()

                print("------------------------------------------")
                print("--Creación de una nueva cuenta--")
                usuarios.addUsuario()
                MenuClientes()
                print("------------------------------------------")
