from prettytable import PrettyTable
from bdPaises import (
    connection,
    getPaisBD,
    insertPaisBD,
    searchPaisById,
    updatePaisBD,
    deletePaisBD,
)


def getAllPaises():
    result = getPaisBD()

    table = PrettyTable()
    table.field_names = ["Id", "Nombre"]

    for pais in result:
        table.add_row([pais["idPaises"], pais["nombre"]])
    print(table)
    table.clear()


def addNewPais():
    print("Se está añadiendo un nuevo País:")
    nombre = input("Nombre: ")
    insertPaisBD(nombre)
    getAllPaises()


def updatePais():
    print("Se está actualizando la información de un país: ")
    id = int(input("Id del país a actualizar: "))
    pais = searchPaisById(id)

    update = int(input("¿Desea actualizar el nombre? 0.No, 1.Sí: "))
    if update == 1:
        print(f"Nombre anterior: {pais['nombre']}")
        nombre = input("Nuevo nombre: ")
    else:
        nombre = pais["nombre"]

    updatePaisBD(nombre, id)
    getAllPaises()


def deletePais():
    print("Se está eliminando un país: ")
    id = int(input("Id del país a eliminar: "))
    deletePaisBD(id)
    getAllPaises()
