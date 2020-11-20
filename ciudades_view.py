from prettytable import PrettyTable
from bdCiudades import (
    connection,
    getCiudadBD,
    insertCiudadBD,
    searchCiudadById,
    updateCiudadBD,
    deleteCiudadBD,
)
from paises_view import tablaPaises


class TablaCiudades:
    def __init__(self):
        self.getAllCiudades()

    def getAllCiudades(self):
        result = getCiudadBD()

        table = PrettyTable()
        table.field_names = [
            "Id",
            "Nombre",
            "IdPais",
            "Nombre del País",
        ]

        for ciudad in result:
            table.add_row(
                [
                    ciudad["idCiudades"],
                    ciudad["nombre"],
                    ciudad["idPaises"],
                    ciudad["nombrePais"],
                ]
            )
        print(table)
        table.clear()

    def addNewCiudad(self):
        print("Se está añadiendo una nueva ciudad: ")
        nombre = input("Nombre: ")
        print("--Tabla Países--")
        tablaPaises()
        idPais = input("Id del país: ")
        insertCiudadBD(nombre, idPais)
        self.getAllCiudades()

    def updateCiudad(self):
        print("Se está actualizando la información de una ciudad: ")
        self.getAllCiudades()
        idCiudad = int(input("Id de la ciudad a actualizar: "))
        ciudad = searchCiudadById(idCiudad)

        update = int(input("¿Desea actualizar el nombre? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Nombre anterior: {ciudad['nombre']}")
            nombre = input("Nuevo nombre: ")
        else:
            nombre = ciudad["nombre"]

        update = int(input("¿Desea actualizar el Id del país? 0.No, 1.Sí: "))
        if update == 1:
            print("--Tabla Países--")
            tablaPaises()
            print(f"Id anterior: {ciudad['idPaises']}")
            idPais = input("Nuevo Id: ")
        else:
            idPais = ciudad["idPaises"]

        updateCiudadBD(nombre, idPais, idCiudad)
        self.getAllCiudades()

    def deleteCiudad(self):
        print("Se está eliminando una ciudad: ")
        self.getAllCiudades()
        idCiudad = int(input("Id de la ciudad a eliminar: "))
        deleteCiudadBD(idCiudad)
        self.getAllCiudades()
