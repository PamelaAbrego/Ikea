from clases_view import tablaClase


class MenuClases:
    def __init__(self):
        print("Bienvenido a la tabla Clases de Productos")
        clase = tablaClase()
        while True:
            print("Menu: ")
            print("0 - Salir. ")
            print("1 - Obtener todas las clases.")
            print("2 - Agregar una nueva clase.")
            print("3 - Actualizar una clase.")
            print("4 - Eliminar una clase")
            option = int(input("Opción: "))

            if option == 0:
                print("Saliendo del menú de Clases de Productos.")
                break
            if option == 1:
                clase.getAllClases()
            if option == 2:
                clase.addNewClase()
            if option == 3:
                clase.updateClase()
            if option == 4:
                clase.deleteClase()
