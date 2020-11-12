from entregas_view import (
    connection,
    getAllEntregas,
    addNewEntrega,
    updateEntrega,
    deleteEntrega,
)

while True:
    print("Entregas")
    print("Menu: ")
    print("0 - Salir. ")
    print("1 - Obtener todas las entregas.")
    print("2 - Agregar una nueva entrega.")
    print("3 - Actualizar una entrega.")
    print("4 - Eliminar una entrega.")
    option = int(input("Opción: "))

    if option == 0:
        print("Saliendo del menú de Entregas")
        connection.close()
        break
    if option == 1:
        getAllEntregas()
    if option == 2:
        addNewEntrega()
    if option == 3:
        updateEntrega()
    if option == 4:
        deleteEntrega()
