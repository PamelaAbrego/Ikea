from categorias_app import MenuCategorias
from ciudades_app import MenuCiudades
from clases_app import MenuClases
from entregas_app import MenuEntregas
from paises_app import MenuPaises
from productos_app import MenuProductos
from usuarios_app import MenuUsuarios


class MenuAdministrador:
    def __init__(self):
        while True:
            print("Bienvenido a la Administración de IKEA")
            print("Menu-Seleccione la tabla que desea administrar:")
            print("0 - Salir. ")
            print("1 - Tabla Usuarios.")
            print("2 - Tabla Productos.")
            print("3 - Tabla Clases de Productos.")
            print("4 - Tabla Categorías de Productos.")
            print("5 - Tabla Carritos de Compras.")
            print("6 - Tabla Facturas.")
            print("7 - Tabla Entregas.")
            print("8 - Tabla Existencias.")
            print("9 - Tabla Sucursales.")
            print("10 - Tabla Ciudades.")
            print("11 - Tabla Países.")
            option = int(input("Opción: "))

            if option == 0:
                print("------------------------------------------")
                print("Saliendo de la Administración de IKEA.")
                print("------------------------------------------")
                break
            if option == 1:
                print("------------------------------------------")
                MenuUsuarios()
                print("------------------------------------------")
            if option == 2:
                print("------------------------------------------")
                MenuProductos()
                print("------------------------------------------")
            if option == 3:
                print("------------------------------------------")
                MenuClases()
                print("------------------------------------------")
            if option == 4:
                print("------------------------------------------")
                MenuCategorias()
                print("------------------------------------------")
            if option == 5:
                # Menú Carrito de Compras
                pass
            if option == 6:
                # Menú Facturas
                pass
            if option == 7:
                print("------------------------------------------")
                MenuEntregas()
                print("------------------------------------------")
                pass
            if option == 8:
                # Menú Existencias
                pass
            if option == 9:
                # Menú Sucursales
                pass
            if option == 10:
                print("------------------------------------------")
                MenuCiudades()
                print("------------------------------------------")
            if option == 11:
                print("------------------------------------------")
                MenuPaises()
                print("------------------------------------------")
