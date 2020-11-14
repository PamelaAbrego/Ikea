from prettytable import PrettyTable
from bdUsuarios import (
    connection,
    getUsuarioBD,
    insertUsuarioBD,
    searchUsuarioById,
    updateUsuarioBD,
    deleteUsuarioBD,
)


def getAllUsuarios():
    result = getUsuarioBD()

    table = PrettyTable()
    table.field_names = [
        "Id",
        "NombreUsuario",
        "Nombre",
        "Apellido",
        "Segundo Apellido",
        "Teléfono",
        "Idioma",
        "Correo Electrónico",
        "Contraseña",
        "Dirección",
    ]

    for usuario in result:
        table.add_row(
            [
                usuario["idUsuarios"],
                usuario["nombreUsuario"],
                usuario["nombre"],
                usuario["apellido"],
                usuario["segundoApellido"],
                usuario["telefono"],
                usuario["idioma"],
                usuario["correoElectronico"],
                usuario["contrasenna"],
                usuario["direccion"],
            ]
        )
    print(table)
    table.clear()


def addNewUsuario():
    print("Se está añadiendo un nuevo Usuario:")
    nombreUsuario = input("Usuario: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    segundoApellido = input("Segundo Apellido: ")
    telefono = input("Teléfono: ")
    idioma = input("Idioma: ")
    correoElectronico = input("Correo Electrónico: ")
    contrasenna = input("Contraseña: ")
    direccion = input("Dirección: ")

    insertUsuarioBD(
        nombreUsuario,
        nombre,
        apellido,
        segundoApellido,
        telefono,
        idioma,
        correoElectronico,
        contrasenna,
        direccion,
    )
    getAllUsuarios()


def updateUsuario():
    print("Se está actualizando la información de un Usuario: ")
    id = int(input("Id del Usuario a actualizar: "))
    usuario = searchUsuarioById(id)
    print(usuario)

    update = int(input("¿Desea actualizar el nombre del usuario? 0.No, 1.Sí: "))
    if update == 1:
        print(f"Nombre anterior: {usuario['nombreUsuario']}")
        nombre = input("Nuevo nombre de Usuario: ")
    else:
        nombre = usuario["nombreUsuario"]

    update = int(input("¿Desea actualizar el nombre? 0.No, 1.Sí: "))
    if update == 1:
        print(f"Nombre anterior: {usuario['nombre']}")
        nombre = input("Nuevo nombre: ")
    else:
        nombre = usuario["nombre"]

    update = int(input("¿Desea actualizar el apellido? 0.No, 1.Sí: "))
    if update == 1:
        print(f"Apellido anterior: {usuario['apellido']}")
        apellido = input("Nuevo apellido: ")
    else:
        apellido = usuario["apellido"]

    update = int(input("¿Desea actualizar el segundo apellido? 0.No, 1.Sí: "))
    if update == 1:
        print(f"Segundo Apellido anterior: {usuario['segundoApellido']}")
        segundoApellido = input("Nuevo Segundo apellido: ")
    else:
        segundoApellido = usuario["segundoApellido"]

    update = int(input("¿Desea actualizar el teléfono? 0.No, 1.Sí: "))
    if update == 1:
        print(f"Teléfono anterior: {usuario['telefono']}")
        telefono = input("Nuevo teléfono: ")
    else:
        telefono = usuario["telefono"]

    update = int(input("¿Desea actualizar el idioma? 0.No, 1.Sí: "))
    if update == 1:
        print(f"Idioma anterior: {usuario['idioma']}")
        idioma = input("Nuevo idioma: ")
    else:
        idioma = usuario["idioma"]

    update = int(input("¿Desea actualizar el correo electrónico? 0.No, 1.Sí: "))
    if update == 1:
        print(f"Correo Electrónico anterior: {usuario['correoElectronico']}")
        correoElectronico = input("Nuevo correo electrónico: ")
    else:
        correoElectronico = usuario["correoElectronico"]

    update = int(input("¿Desea actualizar la contraseña? 0.No, 1.Sí: "))
    if update == 1:
        print(f"Contraseña anterior: {usuario['contrasenna']}")
        contrasenna = input("Nueva contraseña: ")
    else:
        contrasenna = usuario["contrasenna"]

    update = int(input("¿Desea actualizar la dirección? 0.No, 1.Sí: "))
    if update == 1:
        print(f"Dirección anterior: {usuario['direccion']}")
        direccion = input("Nueva dirección: ")
    else:
        direccion = usuario["direccion"]

    updateUsuarioBD(
        nombre,
        apellido,
        segundoApellido,
        telefono,
        idioma,
        correoElectronico,
        contrasenna,
        direccion,
        id,
    )
    getAllUsuarios()


def deleteUsuario():
    print("Se está eliminando un Usuario: ")
    id = int(input("Id del usuario a eliminar: "))
    deleteUsuarioBD(id)
    getAllUsuarios()
