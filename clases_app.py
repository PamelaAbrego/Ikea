from clases_view import (
    connection,
    getAllClases,
    addNewClase,
    updateClase,
    deleteClase,
)


class MenuClases:
    def __init__(self):
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
                getAllClases()
            if option == 2:
                addNewClase()
            if option == 3:
                updateClase()
            if option == 4:
                deleteClase()
