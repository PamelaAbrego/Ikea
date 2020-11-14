from prettytable import PrettyTable
from bdProductos import (
    connection,
    getProductoBD,
    insertProductoBD,
    searchProductoById,
    updateProductoBD,
    deleteProductoBD,
)


def getAllProductos():
    result = getProductoBD()

    table = PrettyTable()
    table.field_names = [
        "Id",
        "Nombre",
        "Precio",
        "Dimensiones",
        "Materiales",
        "Colores Disponibles",
        "Descripción",
        "Garantía",
        "IdClaseProducto",
    ]

    for producto in result:
        table.add_row(
            [
                producto["idProductos"],
                producto["nombre"],
                producto["precio"],
                producto["dimensiones"],
                producto["materiales"],
                producto["coloresDisponibles"],
                producto["descripcion"],
                producto["garantia"],
                producto["idClaseProductos"],
            ]
        )
    print(table)
    table.clear()


def addNewProducto():
    print("Se está añadiendo un nuevo Producto:")
    nombre = input("Nombre: ")
    precio = input("Precio: ")
    dimensiones = input("Dimensiones: ")
    materiales = input("Materiales: ")
    coloresDisponibles = input("Colores disponibles: ")
    descripcion = input("Descripción: ")
    garantia = input("Garantía: ")
    idClaseProductos = input("IdClaseProductos: ")

    insertProductoBD(
        nombre,
        precio,
        dimensiones,
        materiales,
        coloresDisponibles,
        descripcion,
        garantia,
        idClaseProductos,
    )
    getAllProductos()


def updateProducto():
    print("Se está actualizando la información de un Producto: ")
    id = int(input("Id del Producto a actualizar: "))
    producto = searchProductoById(id)

    option = int(input("¿Desea actualizar el nombre? 0.No, 1.Sí: "))
    if option == 1:
        print(f"Nombre anterior: {producto['nombre']}")
        nombre = input("Nuevo nombre: ")

    else:
        nombre = producto["nombre"]

    option = int(input("¿Desea actualizar el precio? 0.No, 1.Sí: "))
    if option == 1:
        print(f"Precio anterior: {producto['precio']}")
        precio = input("Nuevo precio: ")

    else:
        precio = producto["precio"]

    option = int(input("¿Desea actualizar las dimensiones? 0.No, 1.Sí: "))
    if option == 1:
        print(f"Dimensiones anteriores: {producto['dimensiones']}")
        dimensiones = input("Nuevas dimensiones: ")

    else:
        dimensiones = producto["dimensiones"]

    option = int(input("¿Desea actualizar los materiales? 0.No, 1.Sí: "))
    if option == 1:
        print(f"Materiales anteriores: {producto['materiales']}")
        materiales = input("Nuevos materiales: ")

    else:
        materiales = producto["materiales"]

    option = int(input("¿Desea actualizar los colores disponibles? 0.No, 1.Sí: "))
    if option == 1:
        print(f"Colores disponibles anteriores: {producto['coloresDisponibles']}")
        coloresDisponibles = input("Nuevos colores disponibles: ")

    else:
        coloresDisponibles = producto["coloresDisponibles"]

    option = int(input("¿Desea actualizar la descripción? 0.No, 1.Sí: "))
    if option == 1:
        print(f"Descripción anterior: {producto['descripcion']}")
        descripcion = input("Nueva descrpción: ")

    else:
        descripcion = producto["descripcion"]

    option = int(input("¿Desea actualizar la garantía? 0.No, 1.Sí: "))
    if option == 1:
        print(f"Garantía anterior: {producto['garantia']}")
        garantia = input("Nueva garantía: ")

    else:
        garantia = producto["garantia"]

    option = int(input("¿Desea actualizar el IdClaseProducto? 0.No, 1.Sí: "))
    if option == 1:
        print(f"IdClaseProducto anterior: {producto['idClaseProductos']}")
        idClaseProducto = input("Nuevo IdClaseProducto: ")

    else:
        idClaseProducto = producto["idClaseProductos"]

    updateProductoBD(
        nombre,
        precio,
        dimensiones,
        materiales,
        coloresDisponibles,
        descripcion,
        garantia,
        idClaseProducto,
        id,
    )
    getAllProductos()


def deleteProducto():
    print("Se está eliminando un Producto: ")
    id = int(input("Id del producto a eliminar: "))
    deleteProductoBD(id)
    getAllProductos()
