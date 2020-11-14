from ciudades_view import (
    connection,
    getAllCiudades,
    addNewCiudad,
    updateCiudad,
    deleteCiudad,
)


class MenuCiudades:
    def __init__(self):
        while True:
            print("Bienvenido a la tabla Ciudades")
            print("Menu: ")
            print("0 - Salir. ")
            print("1 - Obtener todas las ciudades.")
            print("2 - Agregar una nueva ciudad.")
            print("3 - Actualizar una ciudad.")
            print("4 - Eliminar una ciudad")
            option = int(input("Opción: "))

            if option == 0:
                print("Saliendo del menú de Ciudades.")
                connection.close()
                break
            if option == 1:
                getAllCiudades()
            if option == 2:
                addNewCiudad()
            if option == 3:
                updateCiudad()
            if option == 4:
                deleteCiudad()
