from prettytable import PrettyTable
from bdCategorias import (
    connection,
    getCategoriaBD,
    insertCategoriaBD,
    searchCategoriaById,
    updateCategoriaBD,
    deleteCategoriaBD,
)


def getAllCategorias():
    result = getCategoriaBD()

    table = PrettyTable()
    table.field_names = ["Id", "Nombre"]

    for categoria in result:
        table.add_row([categoria["idCategoriasProductos"], categoria["nombre"]])
    print(table)
    table.clear()


def addNewCategoria():
    print("Se está añadiendo una nueva categoría:")
    nombre = input("Nombre: ")
    insertCategoriaBD(nombre)
    getAllCategorias()


def updateCategoria():
    print("Se está actualizando la información de una categoría: ")
    id = int(input("Id de la categoría a actualizar: "))
    categoria = searchCategoriaById(id)

    update = int(input("¿Desea actualizar el nombre? 0.No, 1.Sí: "))
    if update == 1:
        print(f"Nombre anterior: {categoria['nombre']}")
        nombre = input("Nuevo nombre: ")
    else:
        nombre = categoria["nombre"]

    updateCategoriaBD(nombre, id)
    getAllCategorias()


def deleteCategoria():
    print("Se está eliminando una categoría: ")
    id = int(input("Id de la categoría a eliminar: "))
    deleteCategoriaBD(id)
    getAllCategorias()
