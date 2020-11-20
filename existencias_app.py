from existencias_view import tablaExistencias


class MenuExistencias:
    def __init__(self):
        print("Bienvenido a la tabla Existencias")
        existencias = tablaExistencias()
        while True:
            print("Menu: ")
            print("0 - Salir. ")
            print("1 - Obtener todas las existencias.")
            print("2 - Agregar una nueva existencia.")
            print("3 - Actualizar una existencia.")
            print("4 - Eliminar una existencia")
            option = int(input("Opción: "))

            if option == 0:
                print("Saliendo del menú de Existencias.")
                break
            if option == 1:
                existencias.getAllExistencias()
            if option == 2:
                existencias.addNewExistencia()
            if option == 3:
                existencias.updateExistencia()
            if option == 4:
                existencias.deleteExistencia()
