from prettytable import PrettyTable
from bdExistencias import (
    connection,
    getExistenciaBD,
    insertExistenciaBD,
    searchExistenciaById,
    updateExistenciaBD,
    deleteExistenciaBD,
)
from productos_view import tablaProductos

# FALTA ANCLAR LA TABLA SUCURSALES


class tablaExistencias:
    def __init__(self):
        self.getAllExistencias()

    def getAllExistencias(self):
        result = getExistenciaBD()

        table = PrettyTable()
        table.field_names = [
            "Id",
            "IdProducto",
            "Producto",
            "IdSucursal",
            "Sucursal",
            "Cantidad",
        ]

        for existencia in result:
            table.add_row(
                [
                    existencia["idExistencias"],
                    existencia["idProductos"],
                    existencia["producto"],
                    existencia["idSucursales"],
                    existencia["sucursal"],
                    existencia["cantidad"],
                ]
            )
        print(table)
        table.clear()

    def addNewExistencia(self):
        print("Se está añadiendo una nueva existencia: ")
        print("--Tabla Productos--")
        tablaProductos()
        idProducto = int(input("IdProducto: "))
        # Falta tabla sucursal
        idSucursal = int(input("IdSucursal: "))
        cantidad = int(input("Cantidad: "))
        insertExistenciaBD(idProducto, idSucursal, cantidad)
        self.getAllExistencias()

    def updateExistencia(self):
        print("Se está actualizando la información de una existencia: ")
        self.getAllExistencias()
        idExistencia = int(input("Id de la existencia a actualizar: "))
        existencia = searchExistenciaById(idExistencia)

        update = int(input("¿Desea actualizar el id del Producto? 0.No, 1.Sí: "))
        if update == 1:
            print("--Tabla Productos--")
            tablaProductos()
            print(f"Id del Producto Anterior: {existencia['idProductos']}")
            idProducto = int(input("Nuevo Id del Producto: "))
        else:
            idProducto = existencia["idProductos"]

        update = int(input("¿Desea actualizar el Id de la Sucursal? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Id de la Sucursal anterior: {existencia['idSucursales']}")
            idSucursal = int(input("Nuevo Id de la Sucursal: "))
        else:
            idSucursal = existencia["idSucursales"]

        update = int(input("¿Desea actualizar la cantidad? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Cantidad anterior: {existencia['cantidad']}")
            cantidad = int(input("Nueva cantidad: "))
        else:
            cantidad = existencia["cantidad"]

        updateExistenciaBD(idProducto, idSucursal, cantidad, idExistencia)
        self.getAllExistencias()

    def deleteExistencia(self):
        print("Se está eliminando una existencia: ")
        self.getAllExistencias()
        idExistencia = int(input("Id de la existencia a eliminar: "))
        deleteExistenciaBD(idExistencia)
        self.getAllExistencias()
