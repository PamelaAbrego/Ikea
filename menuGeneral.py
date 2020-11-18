from menuAdministrador import MenuAdministrador
from menuClientes import MenuClientes
from menuRegistro import MenuRegistro

while True:
    print("Bienvenido a IKEA")
    print("----------------------------")
    print("Menú:")
    print("0 - Salir. ")
    print("1 - Ingresar como Administrador.")
    print("2 - Ingresar como Cliente.")

    option = int(input("Opción: "))

    if option == 0:
        print("------------------------------------------")
        print("Saliendo de IKEA.")
        print("------------------------------------------")
        break
    if option == 1:
        print("------------------------------------------")
        MenuAdministrador()
        print("------------------------------------------")
    if option == 2:
        print("------------------------------------------")
        MenuRegistro()
        print("------------------------------------------")
