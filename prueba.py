from categorias_app import menuCategorias


def menuprueba():
    while True:
        print("Menu")
        option = int(input("ingrese opción: "))

        if option == 1:
            menuCategorias()
        else:
            break
