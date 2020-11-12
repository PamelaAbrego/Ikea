from clases_view import (
    connection,
    getAllCategorias,
    addNewCategoria,
    updateCategoria,
    deleteCategoria,
)

while True:
    print("Categorías de Productos")
    print("Menu: ")
    print("0 - Salir. ")
    print("1 - Obtener todas las categorías.")
    print("2 - Agregar una nueva categoría.")
    print("3 - Actualizar una categoría.")
    print("4 - Eliminar una categoría.")
    option = int(input("Opción: "))

    if option == 0:
        print("Saliendo del menú de Categorías de Productos")
        connection.close()
        break
    if option == 1:
        getAllCategorias()
    if option == 2:
        addNewCategoria()
    if option == 3:
        updateCategoria()
    if option == 4:
        deleteCategoria()
