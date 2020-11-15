from prettytable import PrettyTable
from bdClases import (
    connection,
    getClaseBD,
    insertClaseBD,
    searchClaseById,
    updateClaseBD,
    deleteClaseBD,
)
from categorias_view import tablaCategorias


class tablaClase:
    def __init__(self):
        self.getAllClases()

    def getAllClases(self):
        result = getClaseBD()

        table = PrettyTable()
        table.field_names = [
            "Id",
            "Nombre",
            "IdCategoriaProducto",
            "Nombre de la categoría",
        ]

        for clase in result:
            table.add_row(
                [
                    clase["idClaseProductos"],
                    clase["nombre"],
                    clase["idCategoriasProductos"],
                    clase["nombreCategoriaProducto"],
                ]
            )
        print(table)
        table.clear()

    def addNewClase(self):
        print("Se está añadiendo una nueva clase: ")
        nombre = input("Nombre: ")
        print("--Tabla Categorías--")
        tablaCategorias()
        idCategoria = input("Id de la Categoría de Producto: ")
        insertClaseBD(nombre, idCategoria)
        self.getAllClases()

    def updateClase(self):
        print("Se está actualizando la información de una clase: ")
        idClase = int(input("Id de la clase a actualizar: "))
        clase = searchClaseById(idClase)

        update = int(input("¿Desea actualizar el nombre? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Nombre anterior: {clase['nombre']}")
            nombre = input("Nuevo nombre: ")
        else:
            nombre = clase["nombre"]

        update = int(input("¿Desea actualizar el Id de la Categoría? 0.No, 1.Sí: "))
        if update == 1:
            print("--Tabla Categorías--")
            tablaCategorias()
            print(f"Id anterior: {clase['idCategoriasProductos']}")
            idCategoria = input("Nuevo Id: ")
        else:
            idCategoria = clase["idCategoriasProductos"]

        updateClaseBD(nombre, idCategoria, idClase)
        self.getAllClases()

    def deleteClase(self):
        print("Se está eliminando una clase: ")
        idClase = int(input("Id de la clase a eliminar: "))
        deleteClaseBD(idClase)
        self.getAllClases()
