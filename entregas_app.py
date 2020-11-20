from entregas_view import tablaEntregas


class MenuEntregas:
    def __init__(self):
        print("Bienvenido a la tabla Entregas")
        entregas = tablaEntregas()
        while True:
            print("Menu: ")
            print("0 - Salir. ")
            print("1 - Obtener todas las entregas.")
            print("2 - Agregar una nueva entrega.")
            print("3 - Actualizar una entrega.")
            print("4 - Eliminar una entrega.")
            option = int(input("Opción: "))

            if option == 0:
                print("Saliendo del menú de Entregas")
                break
            if option == 1:
                entregas.getAllEntregas()
            if option == 2:
                entregas.addNewEntrega()
            if option == 3:
                entregas.updateEntrega()
            if option == 4:
                entregas.deleteEntrega()
