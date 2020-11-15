from productos_view import tablaProductos
from productos_view import connection


class MenuProductos:
    def __init__(self):
        print("Bienvenido a la tabla Productos: ")
        productos = tablaProductos()
        while True:
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
                productos.getAllProductos()
            if option == 2:
                productos.addNewProducto()
            if option == 3:
                productos.updateProducto()
            if option == 4:
                productos.deleteProducto()
