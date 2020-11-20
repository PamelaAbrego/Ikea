from prettytable import PrettyTable
from bdPaises import (
    connection,
    getPaisBD,
    insertPaisBD,
    searchPaisById,
    updatePaisBD,
    deletePaisBD,
)


class tablaPaises:
    def __init__(self):
        self.getAllPaises()

    def getAllPaises(self):
        result = getPaisBD()

        table = PrettyTable()
        table.field_names = ["Id", "Nombre"]

        for pais in result:
            table.add_row([pais["idPaises"], pais["nombre"]])
        print(table)
        table.clear()

    def addNewPais(self):
        print("Se está añadiendo un nuevo País:")
        nombre = input("Nombre: ")
        insertPaisBD(nombre)
        self.getAllPaises()

    def updatePais(self):
        print("Se está actualizando la información de un país: ")
        self.getAllPaises()
        id = int(input("Id del país a actualizar: "))
        pais = searchPaisById(id)

        update = int(input("¿Desea actualizar el nombre? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Nombre anterior: {pais['nombre']}")
            nombre = input("Nuevo nombre: ")
        else:
            nombre = pais["nombre"]

        updatePaisBD(nombre, id)
        self.getAllPaises()

    def deletePais(self):
        print("Se está eliminando un país: ")
        self.getAllPaises()
        id = int(input("Id del país a eliminar: "))
        deletePaisBD(id)
        self.getAllPaises()
