from paises_view import (
    connection,
    getAllPaises,
    addNewPais,
    updatePais,
    deletePais,
)


class MenuPaises:
    def __init__(self):
        while True:
            print("Bienvenido a la tabla Países")
            print("Menu: ")
            print("0 - Salir. ")
            print("1 - Obtener todos los países.")
            print("2 - Agregar un nuevo país.")
            print("3 - Actualizar un país.")
            print("4 - Eliminar un país.")
            option = int(input("Opción: "))

            if option == 0:
                print("Saliendo del menú de Países")
                connection.close()
                break
            if option == 1:
                getAllPaises()
            if option == 2:
                addNewPais()
            if option == 3:
                updatePais()
            if option == 4:
                deletePais()
