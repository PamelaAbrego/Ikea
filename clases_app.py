from clases_view import tablaClase
from bdClases import connection


class MenuClases:
    def __init__(self):
        print("Bienvenido a la tabla Clases de Productos")
        productos = tablaClase()
        while True:
            print("Bienvenido a la tabla Clases de Productos")
            print("Menu: ")
            print("0 - Salir. ")
            print("1 - Obtener todas las clases.")
            print("2 - Agregar una nueva clase.")
            print("3 - Actualizar una clase.")
            print("4 - Eliminar una clase")
            option = int(input("Opción: "))

            if option == 0:
                print("Saliendo del menú de Clases de Productos")
                connection.close()
                break
            if option == 1:
                productos = tablaClase()
            if option == 2:
                productos.addNewClase()
            if option == 3:
                productos.updateClase()
            if option == 4:
                productos.deleteClase()
