from usuarios_view import (
    connection,
    getAllUsuarios,
    addNewUsuario,
    updateUsuario,
    deleteUsuario,
)

while True:
    print("Usuarios")
    print("Menu: ")
    print("0 - Salir. ")
    print("1 - Obtener todos los usuarios.")
    print("2 - Agregar un nuevo usuario.")
    print("3 - Actualizar un usuario.")
    print("4 - Eliminar un usuario.")
    option = int(input("Opción: "))

    if option == 0:
        print("Saliendo del menú de Usuarios")
        connection.close()
        break
    if option == 1:
        getAllUsuarios()
    if option == 2:
        addNewUsuario()
    if option == 3:
        updateUsuario()
    if option == 4:
        deleteUsuario()
