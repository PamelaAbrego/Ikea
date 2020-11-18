from herramientasClientes import BuscarProducto


class MenuClientes:
    def __init__(self):
        while True:
            print("Bienvenido a la tienda IKEA")
            print("Menu: ")
            print("0 - Regresar.")
            print("1 - Buscar Producto")
            print("2 - ----")

            option = int(input("Opción: "))

            if option == 0:
                print("------------------------------------------")
                print("Saliendo de modo Cliente.")
                print("------------------------------------------")
                break
            if option == 1:
                print("------------------------------------------")
                BuscarProducto()
                print("------------------------------------------")
                break
