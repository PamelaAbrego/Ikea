from productos_view import (
    connection,
    getAllProductos,
    addNewProducto,
    updateProducto,
    deleteProducto,
)


class MenuProductos:
    def __init__(self):
        while True:
            print("Bienvenido a la tabla Productos")
            print("Menu: ")
            print("0 - Salir. ")
            print("1 - Obtener todos los productos.")
            print("2 - Agregar un nuevo producto.")
            print("3 - Actualizar un producto.")
            print("4 - Eliminar un producto.")
            option = int(input("Opción: "))

            if option == 0:
                print("Saliendo del menú de Productos")
                connection.close()
                break
            if option == 1:
                getAllProductos()
            if option == 2:
                addNewProducto()
            if option == 3:
                updateProducto()
            if option == 4:
                deleteProducto()
