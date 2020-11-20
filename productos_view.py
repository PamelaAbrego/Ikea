from prettytable import PrettyTable
from bdProductos import (
    connection,
    getProductoBD,
    insertProductoBD,
    searchProductoById,
    updateProductoBD,
    deleteProductoBD,
)
from clases_view import tablaClase


class tablaProductos:
    def __init__(self):
        self.getAllProductos()

    def getAllProductos(self):
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
            "Nombre Clase Producto",
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
                    producto["nombreClaseProductos"],
                ]
            )
        print(table)
        table.clear()

    def addNewProducto(self):
        print("Se está añadiendo un nuevo Producto:")
        nombre = input("Nombre: ")
        precio = input("Precio: ")
        dimensiones = input("Dimensiones: ")
        materiales = input("Materiales: ")
        coloresDisponibles = input("Colores disponibles: ")
        descripcion = input("Descripción: ")
        garantia = input("Garantía: ")
        print("--Tabla Clases de Productos--")
        tablaClase()
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
        self.getAllProductos()

    def updateProducto(self):
        print("Se está actualizando la información de un Producto: ")
        self.getAllProductos()
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
            print("--Tabla Clases de Productos--")
            tablaClase()
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
        self.getAllProductos()

    def deleteProducto(self):
        print("Se está eliminando un Producto: ")
        self.getAllProductos()
        id = int(input("Id del producto a eliminar: "))
        deleteProductoBD(id)
        self.getAllProductos()
